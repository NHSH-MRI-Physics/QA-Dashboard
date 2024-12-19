import streamlit as st
import pages.Helper as Helper

st.set_page_config(
    page_title="NHSH MRI Dashboard",
    page_icon="🏥",
)

st.header(" NHS Highland MRI Dashboard")

st.markdown(
"""
This is the NHS Highland MRI Dashboard, this contains information on the various QA ran as well as results from said QA. 

Select a component from the side menu. 

### MRI Staff
- John Tracey - John.tracey@nhs.scot
- Jonathan Ashmore - Jonathan.ashmore@nhs.scot
""") 

st.subheader("Current QA Status")

#DQA
sh = Helper.GetSheet()
DQAdates = sh.worksheet("DailyQA").col_values(1)
DQAQAType = sh.worksheet("DailyQA").col_values(2)
DQAResults = sh.worksheet("DailyQA").col_values(3)
DQAScanner = sh.worksheet("DailyQA").col_values(4)

DQAMRI1Index = None
DQAMRI2Index = None
for i, e in reversed(list(enumerate(DQAdates))):
    if DQAScanner[i]=="MRI 1" and DQAMRI1Index==None:
        DQAMRI1Index=i
    if DQAScanner[i] == "MRI 2" and DQAMRI2Index==None:
        DQAMRI2Index=i
    
    if DQAMRI1Index!= None and DQAMRI2Index!= None:
        break

#Distortion
Distortdates = sh.worksheet("DistortionQA").col_values(1)
DistortScanner = sh.worksheet("DistortionQA").col_values(2)
DistortInterplate = sh.worksheet("DistortionQA").col_values(3)
DistortIntraplate = sh.worksheet("DistortionQA").col_values(4)


DistortMRI1Index = None
DistortMRI2Index = None

for i, e in reversed(list(enumerate(Distortdates))):
    if DistortScanner[i]=="Raigmore Hospital MRI 1" and DistortMRI1Index==None:
        DistortMRI1Index=i
    if DistortScanner[i] == "Raigmore Hospital MRI 2" and DistortMRI2Index==None:
        DistortMRI2Index=i
    
    if DistortMRI1Index!= None and DistortMRI2Index!= None:
        break

ResultMRI1 = ":red[Fail]"
if DQAResults[DQAMRI1Index] == "Pass":
    ResultMRI1 = ":green[Pass]"
ResultMRI2 = ":red[Fail]"
if DQAResults[DQAMRI2Index] == "Pass":
    ResultMRI2 = ":green[Pass]"
st.markdown(
f"""
- MRI 1
    * DailyQA
        * Date & Time: {DQAdates[DQAMRI1Index]}
        * QA Type:     {DQAQAType[DQAMRI1Index]}
        * Result:      {ResultMRI1}
- MRI 2
""") 
