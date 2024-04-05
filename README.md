## **Cyber Security Model for Identifying, detecting, and reporting of threats in Bhuvan Portal**
---
#### What is Cybersecurity?
The organization of technologies, procedures, and methods designed to protect networks, devices, programs, and data from attack, damage, malware, viruses, hacking, data theft, or unauthorized access is referred to as cyber security. 

#### Objective of Cybersecurity
The primary goal of cyber security is to protect the confidentiality of all organizational data from both external and internal threats, as well as disruptions caused by natural disasters.


#### Project Objective
Bhuvan is accessed by the users across the world and is prone to cyber-attacks. There are many state-of-art security devices and solutions implemented to tackle the attacks. **However, it is imperative to utilize AI/ ML models to analyze the patterns and Behavior Analysis of the logs collected by the Network Security Devices and to automate alert mechanisms to report the system / network administrators in near- real – time basis**. Therefore, the objective of this project is to :

1. Create a model for identifying and detecting the threats using AI/ ML techniques, analyze cyber attackerbehaviors in Geo-Web Portal and to analyze the user traffic and prepare a report using the given log files.
2. The model created will be able to Identify, Detect and Report the cyber security attacks in the form of PDF file and E-mail alert system.

### Attack Types
We concentrate on four distinct attack types of the **structured server log** to enhance the robustness of our anomaly detection system.

1. **Unusual HTTP Method:** This attack involves the use of unconventional or unauthorized HTTP methods in requests
2. **Unusual Traffic Patterns:** Large fequency of requests in 1s is indicative of potential threats
3. **Random Attacks:** Irregular attempts to breach security
4. **SQL Injection:** A common attack where malicious SQL code is injected into input fields threats.


### Novelty/Approach
1. In our innovative approach, we address the challenge of analyzing massive volumes of raw and unstructured firewall and server logs. 
2. Rather than relying on traditional signature-based parsing methods, we propose the use of **NuLog-based Parsing**, which can outperforms signature-based methods and can effectively parse both firewall and server logs. 
3. This approach involves parsing non-anomalous data logs with NuLog to derive base templates. When real-time data arrives, if its parsed template does not match any base templates, it is flagged as anomalous.
4. To enhance anomaly detection, we employ a **supervised learning** approach. Non-anomalous log templates may miss certain threats, such as unusual traffic patterns or DDoS attacks. Therefore, we develop and train a model using a **Long Short-Term Memory (LSTM)** based on tokenized logs. This involves classifying data, labeling it as normal or specifying the type of attack, and then training the LSTM model for improved threat detection. If an anomaly is identified, an email alert is generated to notify Bhuvan's InfoSec department.
5. (Proposal)Furthermore, we leverage ElasticSearch as an indexing database for efficient storage and manipulation of structured logs. The Elasticsearch-Python connector facilitates the integration of log data with the machine learning model. The predicted results of the anomaly detection model are then written back to the machine learning index in ElasticSearch. To streamline data analysis, we utilize Kibana, a browser-based data visualization dashboard. 
6. This comprehensive approach combines NuLog-based Parsing, supervised learning with LSTM, and advanced data processing techniques to enhance the efficiency and accuracy of anomaly detection in the Bhuvan portal.
![Log Parsing and Data-Preprocessing Methodology](<images/Screenshot 2024-01-21 at 8.56.44 PM.png>)


### Project Pipeline
![Project Pipeline](<images/Screenshot 2024-01-21 at 8.57.42 PM.png>)

### Network Intrusion Detection System Architecture
![Alt text](<images/Screenshot 2024-01-21 at 8.58.24 PM 1.png>)

### Scores
![Model Accuracy](<images/Accuracy Score.JPG>)

### Email/Report template
![Template](<images/Screenshot 2024-01-18 at 8.05.42 PM.png>)

### NuLog Parsed Normal Logs Templates
![NuLog extracted template](<images/Screenshot 2024-01-18 at 8.23.46 PM.png>)


### Running
Open a any new colab notebook, mount the drive and clone the project repository (To run on the system, just clone the repository to the desired location).
The `README.ipynb` file is the main file which contains all the information on how to run this project.

1. Install all the required dependencies by:
``` 
python3 install -r requirements.txt
```
2. Run main.py file to train the model(if and only if the training is required):
```
python3 main.py
```

3. Run test.py file to test the model (edit the path to your server logs in the test.py file):
```
python3 test.py
```
4. Run generate.py to generate the pdf and email alert if any threat is detected.
```
python3 generate.py
```
Note:-
If required, install "wkhtmltopdf" dependency also:
```
sudo apt-get update
sudo apt-get install -y wkhtmltopdf
```

Note: To study more about "Self-Supervised Log Parsing", refer to this [paper](https://arxiv.org/pdf/2003.07905.pdf).

### Future Scope
1. If more data is available, we can better train our NuLog parser and obtain generalized templates for anomaly detection.
2. We can scale our supervised learning model by introducing more types of attacks that can be available in the data logs.
3. E-mail generation can be thresholded to avoid flooding, by adding some time frame in which email should be sent.
4. We can integrate SIEM(Security Information and Event Management) also if real-time data is available.
