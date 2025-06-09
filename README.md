# IDS / DDoS Attack Detection System

**<p align="center">Intrusion Detection System</p>**

<p align="center">
<img src="https://img.shields.io/badge/Roadmap-2025-yellowgreen.svg">
<img src="https://img.shields.io/badge/Author-Mehran%20Nosrati-blue.svg">
<img src="https://img.shields.io/badge/Author-Fatemeh%20Bagheri-blue.svg">
<img src="https://img.shields.io/badge/gu-Golestan%20University-red.svg">
</p>

</br>

- Intrusion Detection System (IDS): A network security tool that monitors network traffic and devices for malicious activity, suspicious activity, or security policy violations. It can be either network-based or host-based.

- NIDS stands for Network Intrusion Detection System. It's a security tool that monitors network traffic for malicious activity, such as attacks, malware, or policy violations, and alerts administrators to potential threats. NIDS are typically passive, meaning they don't actively block attacks, but rather identify them and report them.

- A Distributed Denial-of-Service (DDoS) attack is a type of cyberattack where multiple compromised computers or devices, often a botnet, flood a target server with malicious traffic, making it unavailable to legitimate users. This flood of traffic overwhelms the target's resources, causing a denial of service.

</br>

### Model:

```
model.py
```

### TEST:

```
test.ipynb
```

### Dataset:

CICIDS2017 dataset contains benign and the most up-to-date common attacks, which resembles the true real-world data (PCAPs). It also includes the results of the network traffic analysis using CICFlowMeter with labeled flows based on the time stamp, source, and destination IPs, source and destination ports, protocols and attack (CSV files).

Link: [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html).

### Metrics:

```
Accuracy
Precision
Recall (Sensitivity)
F1 Score
ROC AUC
AUPR (PR-AUC / Average Precision Score)
Sensitivity
Specificity
False Positive Rate (FPR)
False Negative Rate (FNR)
FAR (False Acceptance Rate)
Confusion Matrix
Classification Report
Total Errors
Memory Usage
Runtime
```
