import streamlit as st
from graph import create_workflow

st.set_page_config(page_title="🧭 Travel Chat Assistant", page_icon="🧳")
st.title("🧭 Travel Chat Assistant")
st.markdown("Chat with your AI travel buddy! Hum aapke liye ek perfect trip plan banayenge step-by-step.")

# Initialize session states
if "step" not in st.session_state:
    st.session_state.step = -1  # start with greeting
if "preferences" not in st.session_state:
    st.session_state.preferences = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Static questions
questions = [
    "💰 Aapka budget kya hai?\n- Low (₹5,000 – ₹10,000)\n- Medium (₹10,000 – ₹25,000)\n- High (₹25,000+)\n\nKripya 'low', 'medium' ya 'high' likhiye.",
    "🌍 Aap kis type ki jagah dekhna pasand karte hain? (beach, mountains, heritage, wildlife, spiritual...)",
    "🗓️ Aap kitne din ke liye trip plan kar rahe hain? (jaise: 5)",
    "✅ Kya aap chahenge ki main aapke liye poora travel plan banau? (haan / nahi)"
]

# Initial greeting message
if st.session_state.step == -1:
    greeting = "🙏 Namaste! Main aapka AI travel assistant hoon. Chaliye aapka trip plan karte hain. 😊"
    st.chat_message("assistant").markdown(greeting)
    st.session_state.chat_history.append(("assistant", greeting))

    # Ask first question
    st.session_state.step = 0
    st.chat_message("assistant").markdown(questions[0])
    st.session_state.chat_history.append(("assistant", questions[0]))

# Display history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# Input box
user_input = st.chat_input("Aapka jawaab yahan likhiye...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    step = st.session_state.step

    if step == 0:
        answer = user_input.strip().lower()
        if answer in ["low", "medium", "high"]:
            st.session_state.preferences["budget"] = answer
        else:
            error = "⚠️ Kripya sirf 'low', 'medium' ya 'high' mein se ek option dein."
            st.chat_message("assistant").markdown(error)
            st.session_state.chat_history.append(("assistant", error))
            st.chat_message("assistant").markdown(questions[0])
            st.session_state.chat_history.append(("assistant", questions[0]))
            st.stop()

    elif step == 1:
        interests = [s.strip().lower() for s in user_input.split(",") if s.strip()]
        if interests:
            st.session_state.preferences["interests"] = interests
        else:
            error = "⚠️ Kripya kam se kam ek valid jagah ka type likhiye (jaise: beach, mountains...)."
            st.chat_message("assistant").markdown(error)
            st.session_state.chat_history.append(("assistant", error))
            st.chat_message("assistant").markdown(questions[1])
            st.session_state.chat_history.append(("assistant", questions[1]))
            st.stop()

    elif step == 2:
        try:
            duration = int(user_input.strip())
            if duration <= 0:
                raise ValueError
            st.session_state.preferences["duration"] = duration
        except ValueError:
            error = "⚠️ Kripya valid number mein din likhiye (jaise: 3, 5, 7...)."
            st.chat_message("assistant").markdown(error)
            st.session_state.chat_history.append(("assistant", error))
            st.chat_message("assistant").markdown(questions[2])
            st.session_state.chat_history.append(("assistant", questions[2]))
            st.stop()

    elif step == 3:
        if "haan" in user_input.lower() or "yes" in user_input.lower():
            with st.spinner("🧠 AI trip plan kar raha hai..."):
                graph = create_workflow(st.session_state.preferences)
                result = graph.invoke({})

            # Show final trip info
            st.chat_message("assistant").markdown(f"📍 **Destination:** {result['suggestion']}")
            st.chat_message("assistant").markdown(f"🗺️ **Itinerary:**\n{result['itinerary']}")
            st.chat_message("assistant").markdown(f"🌤️ **Weather & Attractions:**\n{result['support']}")
            st.chat_message("assistant").markdown("🖼️ **Visuals (Images + Hotels):**")

            for line in result["visuals"].split("\n"):
                if line.startswith("http"):
                    st.markdown(f'<img src="{line}" width="300" height="200">', unsafe_allow_html=True)
                else:
                    st.markdown(line)
            st.stop()
        else:
            error = "✅ Jab aap ready ho, bas 'haan' likhiye aur main trip banata hoon."
            st.chat_message("assistant").markdown(error)
            st.session_state.chat_history.append(("assistant", error))
            st.stop()

    # Ask next question if valid step completed
    if step < len(questions) - 1:
        st.session_state.step += 1
        next_q = questions[st.session_state.step]
        st.chat_message("assistant").markdown(next_q)
        st.session_state.chat_history.append(("assistant", next_q))
