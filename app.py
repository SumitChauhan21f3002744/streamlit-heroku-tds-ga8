import streamlit as st

def main():
  st.title("Even or Odd")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Streamlit Even / Odd App <h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  number = st.number_input("Enter a positive number",min_value=0,max_value=1000000000000,step=1)
  result = "Waiting for the number..."
  if st.button("Check"):
    result = "Even" if number%2 == 0 else "Odd"
  st.success(f"The given number is {result}")
  if st.button("About"):
    st.text("Lets Learn")
    st.text("Built with Streamlit")
if __name__ == "__main__":
  main()
