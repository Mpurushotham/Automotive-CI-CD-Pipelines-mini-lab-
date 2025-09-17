'''goovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/automotive-ci-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'make clean && make'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pytest tests/test_main.py --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Dockerized Build Env') {
            steps {
                sh 'docker build -t automotive-ci-demo .'
                sh 'docker run --rm automotive-ci-demo ./bin/main'
            }
        }

        stage('Deploy to Hardware (Simulated)') {
            steps {
                sh 'bash scripts/deploy.sh'
            }
        }

        stage('Log Parsing') {
            steps {
                sh 'python3 scripts/parse_logs.py > build_logs.json'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/bin/*, **/*.json', fingerprint: true
            }
        }
    }
}
'''
