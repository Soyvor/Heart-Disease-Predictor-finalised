def main():
    # Set app title
    st.title('Heart Disease Prediction')

    # Display the dataset
    st.write('**Dataset Overview:**')
    st.write(df.head())

    # Collect user inputs
    st.sidebar.title('User Input')
    user_inputs = {}

    for column in df.columns:
        # Allow user to input values based on dataset columns
        user_inputs[column] = st.sidebar.selectbox(f'Select {column}', df[column].unique())

    # Convert user inputs into DataFrame
    user_data = pd.DataFrame([user_inputs])

    # Make predictions
    if st.sidebar.button('Predict'):
        prediction = svm_model.predict(user_data)
        if prediction[0] == 1:
            st.write('**Prediction:** You are predicted to have heart disease.')
        else:
            st.write('**Prediction:** You are predicted to be healthy.')

if __name__ == '__main__':
    main()
