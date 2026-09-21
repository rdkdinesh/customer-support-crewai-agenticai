import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool


# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY is missing in the .env file.")
    st.stop()

if not SERPER_API_KEY:
    st.error("SERPER_API_KEY is missing in the .env file.")
    st.stop()


# ============================================================
# 2. STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# 3. CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .agent-card {
        padding: 20px;
        border-radius: 12px;
        background-color: #f5f7fa;
        margin-bottom: 15px;
        border: 1px solid #e1e5eb;
    }

    .agent-title {
        font-size: 20px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. APPLICATION HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 AI Customer Support Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Multi-Agent Customer Support using CrewAI'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 5. SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🧠 Multi-Agent Architecture")

    st.markdown(
        """
        **Agent 1 – FAQ Agent**

        📚 Searches the local FAQ knowledge base.

        ---

        **Agent 2 – Web Search Agent**

        🌐 Searches the internet for additional information.

        ---

        **Agent 3 – Logger Agent**

        💾 Saves Agent 1 and Agent 2 responses locally.
        """
    )

    st.divider()

    st.info(
        "Ask a customer-support question using the chat box."
    )


# ============================================================
# 6. LOAD LOCAL FAQ
# ============================================================

FAQ_FILE = "faq.txt"
LOG_FILE = "customer_support_log.txt"


def load_faq():

    if not os.path.exists(FAQ_FILE):

        return "FAQ file not found."

    with open(
        FAQ_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


faq_content = load_faq()


# ============================================================
# 7. WEB SEARCH TOOL
# ============================================================

search_tool = SerperDevTool(api_key=SERPER_API_KEY)


# ============================================================
# 8. CREATE AGENT 1 - FAQ AGENT
# ============================================================

faq_agent = Agent(

    role="Customer FAQ Specialist",

    goal=(
        "Answer customer questions using the provided "
        "local FAQ knowledge base."
    ),

    backstory=(
        "You are a customer support specialist. "
        "You carefully read the local FAQ information "
        "and provide accurate answers. "
        "You must not invent FAQ information."
    ),

    verbose=True,

    allow_delegation=False
)


# ============================================================
# 9. CREATE AGENT 2 - WEB SEARCH AGENT
# ============================================================

web_agent = Agent(

    role="Web Research Customer Support Specialist",

    goal=(
        "Search the internet and provide useful and "
        "current information for customer questions."
    ),

    backstory=(
        "You are an online research specialist working "
        "for a customer support team. "
        "When local FAQ information is insufficient, "
        "you research the web and summarize relevant information."
    ),

    tools=[search_tool],

    verbose=True,

    allow_delegation=False
)


# ============================================================
# 10. CREATE AGENT 3 - LOGGER AGENT
# ============================================================

logger_agent = Agent(

    role="Customer Support Audit Specialist",

    goal=(
        "Prepare a structured support record containing "
        "the customer query and responses from the other agents."
    ),

    backstory=(
        "You maintain customer support records. "
        "Your job is to organize Agent 1 and Agent 2 responses "
        "into a clear audit-friendly format."
    ),

    verbose=True,

    allow_delegation=False
)


# ============================================================
# 11. STREAMLIT CHAT INPUT
# ============================================================

customer_query = st.chat_input(
    "💬 Ask your customer-support question..."
)


# ============================================================
# 12. PROCESS CUSTOMER QUERY
# ============================================================

if customer_query:

    # --------------------------------------------------------
    # Display customer message
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.markdown(customer_query)


    # ========================================================
    # AGENT 1 TASK
    # ========================================================

    faq_task = Task(

        description=f"""
        Customer Query:

        {customer_query}

        Local FAQ Knowledge Base:

        {faq_content}

        Instructions:

        1. Analyze the customer question.
        2. Search the provided FAQ knowledge.
        3. If the FAQ contains relevant information,
           provide a concise customer-friendly answer.
        4. If the FAQ does not contain relevant information,
           clearly state:

           "NO_RELEVANT_FAQ_FOUND"

        Do not invent information.
        """,

        expected_output=(
            "A concise FAQ-based answer or "
            "NO_RELEVANT_FAQ_FOUND."
        ),

        agent=faq_agent
    )


    # ========================================================
    # AGENT 2 TASK
    # ========================================================

    web_task = Task(

        description=f"""
        Customer Query:

        {customer_query}

        Perform web research for this customer query.

        Provide:

        1. Relevant information
        2. Current information when applicable
        3. A concise customer-friendly explanation

        Do not provide unrelated information.
        """,

        expected_output=(
            "A concise web-researched customer support answer."
        ),

        agent=web_agent
    )


    # ========================================================
    # AGENT 3 TASK
    # ========================================================

    logger_task = Task(

        description=f"""
        Customer Query:

        {customer_query}

        Organize the customer-support interaction.

        Include:

        Customer Query:
        {customer_query}

        Agent 1 FAQ Response:
        Use the result from Agent 1.

        Agent 2 Web Response:
        Use the result from Agent 2.

        Create a clean audit record.

        Do not add new information.
        """,

        expected_output=(
            "A structured customer support audit record."
        ),

        agent=logger_agent
    )


    # ========================================================
    # CREATE CREW
    # ========================================================

    crew = Crew(

        agents=[
            faq_agent,
            web_agent,
            logger_agent
        ],

        tasks=[
            faq_task,
            web_task,
            logger_task
        ],

        process=Process.sequential,

        verbose=True
    )


    # ========================================================
    # EXECUTE CREW
    # ========================================================

    with st.spinner(
        "🤖 AI agents are processing your request..."
    ):

        try:

            result = crew.kickoff()

        except Exception as e:

            st.error(
                f"Error while executing CrewAI: {str(e)}"
            )

            st.stop()


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.subheader("🤖 Customer Support Response")

    #st.write(result)
    st.markdown(result)


    # ========================================================
    # SAVE RESULT TO LOCAL FILE
    # ========================================================

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    log_content = f"""
============================================================
CUSTOMER SUPPORT INTERACTION
============================================================

Timestamp:
{timestamp}

Customer Query:
{customer_query}

CrewAI Response:
{result}

============================================================

"""


    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(log_content)


    st.success(
        f"✅ Interaction saved to {LOG_FILE}"
    )


# ============================================================
# 13. FOOTER
# ============================================================

st.divider()

st.caption(
    "Built with Streamlit + CrewAI + Multi-Agent AI"
)