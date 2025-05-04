# Purpose of file: Project main file.

import streamlit as st
from truth_table import TruthTable

if __name__ == "__main__":

   st.set_page_config("Truth Table Creator")


   st.title("Truth Table Creator")

   truth_table = TruthTable("AvB")

   formula = st.text_input("Logical Expression:", help="Type in a logical expression here to create a truth table")

   
   if formula:
      st.table(TruthTable(formula).generate_truth_table())