if page=='update data':
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='Vivek@634163#',database='miniproject',auth_plugin='mysql_native_password')
        name=st.text_input("USERNAME:","")
        st.text("")
        st.text("")
        st.text("")
        PSS=st.text_input("PASSWORD:","")
        if(None):
          st.title(">>> UPDATE DATA IN A CSV FILE <<<")
          st.text("")
          st.text("")
          st.text("")
          name=st.text_input("Enter name of country:","")
          st.text("")
          deaths=st.number_input("Enter number of deaths:",min_value=0,max_value=10000000,step=1)
          st.text("")
          confirmed=st.number_input("Enter number of confirmed cases:",min_value=0,max_value=10000000,step=1)
          st.text("")
          recovered=st.number_input("Enter number of recovered cases:",min_value=0,max_value=10000000,step=1)
          st.text("")
          active=st.number_input("Enter number of active cases:",min_value=0,max_value=10000000,step=1)
          st.text("")
          st.text("")
          st.text("")
          res=st.button("Save")
          if res:
           name=name[0].upper()+name[1:]
           df.loc[df['Country/Region']==name,'Confirmed']=confirmed
           df.loc[df['Country/Region']==name,'Deaths']=deaths
           df.loc[df['Country/Region']==name,'Recovered']=recovered
           df.loc[df['Country/Region']==name,'Active']=active
           df.to_csv("country_wise_latest.csv",index=False)
