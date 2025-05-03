# Purpose of file: Project main file.

import streamlit as st
from truth_table import TruthTable

if __name__ == "__main__":
   truth_table = TruthTable("AvB")

   formula = st.text_input("Logical Expression:")
   
   if formula:
      st.table(TruthTable(formula).generate_truth_table())