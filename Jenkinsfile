
pipeline {
    agent {
        label 'windows-agent'
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Tools') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat '.venv\\Scripts\\python.exe -m playwright install chromium'
            }
        }

        stage('Run UI and API Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'if not exist test-results mkdir test-results'
                bat '.venv\\Scripts\\python.exe -m pytest -v --browser chromium --junitxml=reports\\junit.xml --html=reports\\report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'reports/junit.xml'

            archiveArtifacts artifacts: 'reports/**,test-results/**',
                             allowEmptyArchive: true
        }
    }
}
