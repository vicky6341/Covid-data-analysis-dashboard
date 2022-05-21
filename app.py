#importing requred modules
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import mysql.connector



df=pd.read_csv('country_wise_latest.csv')

st.set_page_config(page_title="covid analysis",
                   layout="wide")

st.sidebar.title("visualization selector")

page_names=['Overall analysis','Country wise analysis','Login']

page=st.sidebar.radio('select an option:',page_names)



if page=='html':
        st.markdown(html_string,unsafe_allow_html=True)


if page=='Overall analysis':
        st.title(">>>>>>>>>>>>>>>     COVID ANALYSIS     <<<<<<<<<<<<<<")
        st.text("")
        st.text("")
        st.subheader("Covid status of different countries:")
        st.dataframe(df)
        st.text("")
        st.text("")
        st.subheader("Top 10 countries with highest number of deaths:")
        b=df.nlargest(10,'Deaths')
        st.dataframe(b)
        if st.checkbox('Bar chart',False,key=2):
            st.bar_chart(b['Deaths'])
        st.text("")
        st.text("")
        st.subheader("Top 10 countries with lowest number of deaths:")
        b=df.nsmallest(10,'Deaths')
        st.dataframe(b)
        b_cou_list=b["Country/Region"].values.tolist()
        b_active_list=b["Active"].values.tolist()
        b=pd.DataFrame({
                'index':b_cou_list,
                'Active':b_active_list,
                }).set_index('index')
        if st.checkbox('Bar chart',False,key=3):
            st.bar_chart(b)
        
    
        







    
        






def get_total_dataframe(dataset):
    total_dataframe=pd.DataFrame({'Status':['Confirmed','Recovered','Deaths','Active'],
                                  'Number of cases':(dataset.iloc[0]['Confirmed'],dataset.iloc[0]['Recovered'],dataset.iloc[0]['Deaths'],dataset.iloc[0]['Active'])})
    return total_dataframe

country_total=get_total_dataframe(df)




if page=='Country wise analysis':
    select=st.sidebar.selectbox('select a country',df['Country/Region'])
    country_data=df[df['Country/Region']==select]

    confirm=country_data.iloc[0]['Confirmed']
    recovered=country_data.iloc[0]['Recovered']
    deaths=country_data.iloc[0]['Deaths']
    active=country_data.iloc[0]['Active']

             
    st.title("    >>>>>> COVID STATUS OF %s <<<<<<<"%(select))
    st.text("")
    st.text("")
    st.text("")

    st.markdown("*Number of confirmed cases  are                                                    = **_%d_**"%(confirm))
    st.markdown("*Number of recovered cases  are                                                    = **_%d_**"%(recovered))
    st.markdown("*Number of death cases are                                                    = **_%d_**"%(deaths))
    st.markdown("*Number of active cases  are                                                    = **_%d_**"%(active))

    st.text("")
    st.text("")
    st.text("")

   
    st.subheader("Bar chart representation:")           
    c_t_g=px.bar(country_total,x='Status',y='Number of cases',labels={'Number of cases':'Number of cases in %s'% (select)},color='Status')
    st.plotly_chart(c_t_g)
    st.text("")
    st.text("")
    st.subheader("Pie chart representation:")

  
    fig=px.pie(country_data,values=[confirm,recovered,deaths,active],names=['Confirmed','Recovered','Deaths','Active'])
    st.plotly_chart(fig)





if page=='Login':
        st.title(">>> Login(only admin can update data)<<<")
        user=st.text_input("Enter user name:","")
        st.text("")
        st.text("")
        password=st.text_input("Enter password:","")
        st.text("")
        st.text("")
        if 'counter' not in st.session_state:
            st.session_state.counter=False
        if st.button("login") or st.session_state.counter:
                st.session_state.counter=True
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='Vivek@634163#',database='miniproject',auth_plugin='mysql_native_password',port='3306')
                cursor=mydb.cursor(buffered=True)
                cursor.execute("select * from user where user_name='vivek' ")
                data=cursor.fetchall()
                if len(data)!=0:
                     if(data[0][0]==user and data[0][1]==password):
                                 
                                 st.title(">>> UPDATE DATA IN A CSV FILE <<<")
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
                                 
                                 if st.button("Save"):
                                     name=name[0].upper()+name[1:]
                                     df.loc[df['Country/Region']==name,'Confirmed']=confirmed
                                     df.loc[df['Country/Region']==name,'Deaths']=deaths
                                     df.loc[df['Country/Region']==name,'Recovered']=recovered
                                     df.loc[df['Country/Region']==name,'Active']=active
                                     df.to_csv("country_wise_latest.csv",index=False)
                                     st.markdown("successfully saved")
                               
                     else:
                      st.markdown("give valid credentials")
           
                
        
        
        
        



    
    
    
    






    
