pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "mkdir build || true; cd build; cmake ..; make test"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.... (skip)'
            }
        }
    }
}
