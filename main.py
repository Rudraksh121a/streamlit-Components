import streamlit as st

# Set the app title
st.title("Streamlit Components")

with st.expander("st.title()"):
    st.code("""
st.title("This is a Title")
    """)
    st.title("THIS IS TITLE")
    st.write("Use `st.title()` to display the main title of your Streamlit app.")

with st.expander("st.header()"):
    st.code("""
st.header("This is a Header")
    """)
    st.header("THIS IS HEADER")
    st.write("Use `st.header()` to display a section header in your app.")

with st.expander("st.subheader()"):
    st.code("""
st.subheader("This is a Subheader")
    """)
    st.subheader("THIS IS SUBHEADER")
    st.write("Use `st.subheader()` to display a subheading or subheader for a specific section.")

with st.expander("st.text()"):
    st.code("""
st.text("This is plain text")
    """)
    st.text("THIS IS TEXT")
    st.write("Use `st.text()` to display plain text without any formatting.")

with st.expander("st.markdown()"):
    st.code("""
st.markdown('**Bold Text** and *Italic Text*')
    """)
    st.markdown("**Bold Text** and *Italic Text*")
    st.write("Use `st.markdown()` to render text with Markdown formatting, such as bold or italics.")

with st.expander("st.code()"):
    st.code("""
st.code('import streamlit as st')
    """)
    st.code('import streamlit as st')
    st.write("Use `st.code()` to display a block of code with syntax highlighting.")

with st.expander("st.latex()"):
    st.code("""
st.latex(r'a^2 + b^2 = c^2')
    """)
    st.latex(r'a^2 + b^2 = c^2')
    st.write("Use `st.latex()` to render LaTeX math expressions in your app.")

with st.expander("st.write()"):
    st.code("""
st.write("Hello World!")
st.write([1, 2, 3, 4])
    """)
    st.write("Hello World!")
    st.write([1, 2, 3, 4])
    st.write("Use `st.write()` to display a wide variety of data types like text, lists, and more.")

with st.expander("st.button()"):
    st.code("""
if st.button('Click Me'):
    st.write('Button was clicked!')
    """)
    if st.button('Click Me'):
        st.write('Button was clicked!')
    st.write("Use `st.button()` to display a button and perform an action when it's clicked.")

with st.expander("st.text_input()"):
    st.code("""
user_input = st.text_input('Enter your name:')
if user_input:
    st.write(f'Hello {user_input}!')
    """)
    user_input = st.text_input('Enter your name:')
    if user_input:
        st.write(f'Hello {user_input}!')
    st.write("Use `st.text_input()` to create a text input field.")

with st.expander("st.number_input()"):
    st.code("""
number = st.number_input('Enter a number:', min_value=1, max_value=100)
st.write(f'You entered: {number}')
    """)
    number = st.number_input('Enter a number:', min_value=1, max_value=100)
    st.write(f'You entered: {number}')
    st.write("Use `st.number_input()` to create a numeric input widget.")

with st.expander("st.selectbox()"):
    st.code("""
option = st.selectbox('Choose a color:', ['Red', 'Blue', 'Green'])
st.write(f'You selected: {option}')
    """)
    option = st.selectbox('Choose a color:', ['Red', 'Blue', 'Green'])
    st.write(f'You selected: {option}')
    st.write("Use `st.selectbox()` to create a dropdown menu.")

with st.expander("st.multiselect()"):
    st.code("""
options = st.multiselect('Pick some fruits:', ['Apple', 'Banana', 'Orange'])
st.write(f'You selected: {options}')
    """)
    options = st.multiselect('Pick some fruits:', ['Apple', 'Banana', 'Orange'])
    st.write(f'You selected: {options}')
    st.write("Use `st.multiselect()` to create a multi-select widget for choosing multiple options.")

with st.expander("st.slider()"):
    st.code("""
age = st.slider('Select your age', 0, 100)
st.write(f'Your age is: {age}')
    """)
    age = st.slider('Select your age', 0, 100)
    st.write(f'Your age is: {age}')
    st.write("Use `st.slider()` to create a slider for selecting values from a range.")

with st.expander("st.file_uploader()"):
    st.code("""
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write("File uploaded successfully!")
    """)
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        st.write("File uploaded successfully!")
    st.write("Use `st.file_uploader()` to allow users to upload files to your app.")

with st.expander("st.progress()"):
    st.code("""
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    """)
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
    st.write("Use `st.progress()` to display a progress bar that shows completion.")

with st.expander("st.spinner()"):
    st.code("""
with st.spinner('Loading...'):
    import time
    time.sleep(2)
st.success('Done!')
    """)
    with st.spinner('Loading...'):
        import time
        time.sleep(2)
    st.success('Done!')
    st.write("Use `st.spinner()` to display a spinner while a task is running.")

with st.expander("st.table()"):
    st.code("""
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
st.table(df)
    """)
    import pandas as pd
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    st.table(df)
    st.write("Use `st.table()` to display a static table.")

with st.expander("st.dataframe()"):
    st.code("""
st.dataframe(df)
    """)
    st.dataframe(df)
    st.write("Use `st.dataframe()` to display an interactive dataframe.")

with st.expander("st.json()"):
    st.code("""
st.json({'name': 'Alice', 'age': 25})
    """)
    st.json({'name': 'Alice', 'age': 25})
    st.write("Use `st.json()` to display JSON data in a readable format.")

with st.expander("st.chat_message()"):
    st.code("""
st.chat_message("user").write("Hello!")
st.chat_message("assistant").write("Hi there!")
    """)
    st.chat_message("user").write("Hello!")
    st.chat_message("assistant").write("Hi there!")
    st.write("Use `st.chat_message()` to create a chat interface for user interaction.")

with st.expander("st.expander()"):
    st.code("""
with st.expander("See more"):
    st.write("Here is some more information!")
    """)


with st.expander("st.columns()"):
    st.code("""
col1, col2, col3 = st.columns(3)
col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")
    """)
    col1, col2, col3 = st.columns(3)
    col1.write("Column 1")
    col2.write("Column 2")
    col3.write("Column 3")
    st.write("Use `st.columns()` to create multiple columns in your app.")

with st.expander("st.container()"):
    st.code("""
with st.container():
    st.write("This is inside a container.")
    """)
    with st.container():
        st.write("This is inside a container.")
    st.write("Use `st.container()` to group components together within a container.")

with st.expander("st.select_slider()"):
    st.code("""
option = st.select_slider('Choose a range:', options=['Low', 'Medium', 'High'])
st.write(f'You selected: {option}')
    """)
    option = st.select_slider('Choose a range:', options=['Low', 'Medium', 'High'])
    st.write(f'You selected: {option}')
    st.write("Use `st.select_slider()` to create a slider with specific options.")

with st.expander("st.metric()"):
    st.code("""
st.metric(label="Temperature", value="70 °F", delta="1 °F")
    """)
    st.metric(label="Temperature", value="70 °F", delta="1 °F")
    st.write("Use `st.metric()` to display a metric with a value and optional delta change.")

with st.expander("st.session_state"):
    st.code("""
if 'counter' not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.write(f'Counter: {st.session_state.counter}')
    """)
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    st.session_state.counter += 1
    st.write(f'Counter: {st.session_state.counter}')
    st.write("Use `st.session_state` to store and persist state across app reruns.")
