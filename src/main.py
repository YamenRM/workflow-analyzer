from analyzer import analyze_workflow
import streamlit as st

st.title("Ai Workflow Analyzer")

st.write("Type your workflow to analyze its structure and components.")

st.text_area("Workflow Input", height=200, key="workflow_input")

if st.button("Analyze Workflow"):
    workflow_input = st.session_state.workflow_input
    if workflow_input:
        analysis_result = analyze_workflow(workflow_input)
        st.subheader("Analysis Result")
        st.write(analysis_result)

        st.download_button(
            label="Download Analysis Result",
            data=analysis_result,
            file_name="analysis_result.md",
            mime="text/plain"
        )
    else:
        st.warning("Please enter a workflow to analyze.")

    
st.write("© 2026 Ai Workflow Analyzer. All rights reserved.")




  
   