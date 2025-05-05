# Purpose of file: Project main file.

import streamlit as st
from truth_table import TruthTable

if __name__ == "__main__":

   st.set_page_config("Truth Table Creator")


   st.title("Truth Table Creator")

   truth_table = TruthTable("AvB")

   formula = st.text_input("Logical Expression:", 
                           help="Type in a logical expression here to create a truth table",
                           max_chars=50)

   
   if formula:
      try:
         st.table(TruthTable(formula).generate_truth_table())
      except Exception as E:
         st.text(f"Error: {E}\nMore error support coming soon, for now just check your parenthesis, atoms, and operators")