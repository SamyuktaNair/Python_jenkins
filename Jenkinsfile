pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SamyuktaNair/Python_jenkins.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml
                '''
            }
        }

        stage('Publish Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
