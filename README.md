# Automotive-CI-CD-Pipelines-mini-lab-
Automotive CI-CD-Pipelines mini lab project structure to illustrate how to setup

# 🚗 Mini Project: Automotive CI/CD Pipeline in Jenkins

# Tech Stack
*		Jenkins (automation server)
*		Gerrit/GitHub (source control)
*		Docker (isolated build environment)
*		Make + C/C++ (compilation)
*		Python (test automation, log parsing)
*		Bash/PowerShell (infra scripting)
*		Artifact storage (Jenkins workspace or Azure blob simulation)

## project structure >

automotive-ci-demo/

*	│── src/
*	│   └── main.c            # Simple C program (simulating ECU software)
*	│   └── Makefile          # Build rules
*	│── tests/
*	│   └── test_main.py      # Python unit test
*	│── scripts/
*	│   └── deploy.sh         # Simulated hardware deployment
*	│   └── parse_logs.py     # Log parsing script
*	│── Jenkinsfile           # CI/CD pipeline definition

# 🔹 Workflow Diagram (End-to-End) >

##   Code → Gerrit → Jenkins → Build → Unit Test → Docker Build → Deploy to Hardware → Parse Logs → Store Artifacts


<img width="1327" height="800" alt="image" src="https://github.com/user-attachments/assets/7d87f92b-e12e-49ef-81b3-dc1d114676d4" />

=============================================================================

<img width="1153" height="800" alt="image" src="https://github.com/user-attachments/assets/05d0681e-60df-4f6c-9b0a-a4ed42c2bd36" />

# Process Steps

## 🚀 Mini Project: End-to-End CI/CD Pipeline with Jenkins

🎯 Goal

## Set up a Jenkins pipeline that:
	1.	Pulls source code from GitHub/Gerrit.
	2.	Builds a Docker image of the app (simulating ECU software).
	3.	Runs static code analysis (SonarQube).
	4.	Runs unit tests inside a container.
	5.	Deploys to a Kubernetes cluster (simulating ECU test rigs).
	6.	Sends logs/metrics to Azure Monitor or Prometheus + Grafana.

## 🛠 Required Tools
	•	Git/Gerrit → Source code repo
	•	Jenkins → CI/CD orchestrator
	•	Docker → Container build
	•	SonarQube → Static analysis
	•	Kubernetes (Minikube/Kind/AKS) → Deployment/test environment
	•	Argo CD (optional) → GitOps style deployment
	•	Prometheus + Grafana → Monitoring

# 📂 Project Workflow

## 1. Code Commit Stage
	•	Developer pushes code → GitHub/Gerrit.
	•	Webhook triggers Jenkins pipeline.

 ```
git add .
git commit -m "New ECU feature"
git push origin main
```

## 2. Build Stage
	•	Jenkins clones repo.
	•	Docker builds application image with Dockerfile.

👉 Pipeline snippet:

```groovy
stage('Build Docker Image') {
    steps {
        sh 'docker build -t ecu-app:${BUILD_NUMBER} .'
    }
}
```

## 3. Static Code Analysis Stage
	•	Run SonarQube scan for vulnerabilities & code smells.

👉 Pipeline snippet:

```groovy
stage('Static Analysis') {
    steps {
        sh 'sonar-scanner -Dsonar.projectKey=ecu-app -Dsonar.host.url=http://sonarqube:9000'
    }
}
```

## 4. Test Stage
	•	Run unit & integration tests inside Docker container.

👉 Pipeline snippet:

```groovy
stage('Run Tests') {
    steps {
        sh 'docker run ecu-app:${BUILD_NUMBER} pytest tests/'
    }
}
```

## 5. Deploy Stage
	•	Push Docker image to registry (DockerHub/Azure Container Registry).
	•	Deploy app to Kubernetes cluster.

👉 Pipeline snippet:

```groovy
stage('Deploy to K8s') {
    steps {
        sh 'kubectl apply -f k8s/deployment.yaml'
        sh 'kubectl rollout status deployment/ecu-app'
    }
}
```

## 6. Monitoring & Logging
	•	Logs streamed via Fluentd/EFK stack → Azure Monitor.
	•	Metrics collected via Prometheus → visualized in Grafana dashboard.

👉 Pipeline snippet:

```groovy
stage('Post-Deployment Monitoring') {
    steps {
        sh 'kubectl logs -l app=ecu-app --tail=100'
    }
}
```

## End-to-End Workflow Diagram

 [!TIP] Developer → Git Commit → Jenkins → Build (Docker) → Static Scan (SonarQube) → Unit Tests (pytest) → Deploy to K8s → Monitor (Prometheus/Grafana)

 


