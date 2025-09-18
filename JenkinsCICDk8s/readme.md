# 🚀 Step-by-Step Execution Guide for Jenkins CI/CD Project

## 1. Setup Jenkins Environment
	•	Access Jenkins: http://localhost:8080
	•	Install required plugins: Pipeline, Docker, Kubernetes, Git, SonarQube Scanner

```bash
# On Ubuntu (example)
sudo apt update && sudo apt install -y openjdk-11-jdk git docker.io

# Add Jenkins repo and install
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update && sudo apt install -y jenkins

# Start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

## 2. Integrate GitHub Repo
	•	Create a repo: ecu-app
	•	Push provided project files (Jenkinsfile, Dockerfile, app.py, tests/, k8s/)
	•	Connect Jenkins with GitHub (via Webhook or Poll SCM)


## 3. Configure Jenkins Pipeline
	1.	Create a Pipeline job in Jenkins.
	2.	Select Pipeline script from SCM → Git → Paste repo URL.
	3.	Save & Build.

## 4. Pipeline Stages Explained
  
  Stage 1: Checkout
  
  * 👉 Pulls latest code from GitHub.

  ```groovy
git branch: 'main', url: 'https://github.com/your-username/ecu-app.git'
```
Stage 2: Build Docker Image

* 👉 Creates container image with your app.

```bash
docker build -t docker.io/your-docker-username/ecu-app:$BUILD_NUMBER .
```
Stage 3: Static Code Analysis

* 👉 Ensures code quality using SonarQube.

```bash
sonar-scanner \
  -Dsonar.projectKey=ecu-app \
  -Dsonar.host.url=http://sonarqube:9000
```
Stage 4: Run Unit Tests

* 👉 Executes tests inside container.

  ```bash
  docker run docker.io/your-docker-username/ecu-app:$BUILD_NUMBER pytest tests/
  ```

  Stage 5: Push Image to Registry

  * 👉 Stores versioned image in Docker Hub.

```bash
docker push docker.io/your-docker-username/ecu-app:$BUILD_NUMBER
```

Stage 6: Deploy to Kubernetes

* 👉 Deploys updated app to Kubernetes cluster.

  ```bash
  kubectl apply -f k8s/deployment.yaml
  kubectl rollout status deployment/ecu-app
  ```
Stage 7: Post-Deployment Logs

* 👉 Shows real-time logs from pods.

```bash
kubectl logs -l app=ecu-app --tail=50
```

5. Access the App

* 	Get external IP:

```bash
  kubectl get svc ecu-app-service
```
* Open in browser:

> [!NOTE]
> http://<external-ip> → "Hello from ECU App CI/CD Pipeline!"

## Conclusion: 
	•	You built from scratch: GitHub → Jenkins Pipeline → Docker → SonarQube → Pytest → Kubernetes → Monitoring.
	•	Each step represents automation & reliability.
	•	You can extend this with:
	•	CAN bus ECU integration (future automotive use case)
	•	Azure cloud deployment (extend Service → LoadBalancer with Azure)
	•	Vector Canoe testing (for hardware-in-the-loop CI/CD).

> [!TIP]
>  Troubleshoot the CI and CD service connection issues and analyse Why some plugins are mandatory and how to integrated security tools into stages.

