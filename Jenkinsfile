pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh "mkdir build || true; cd build && cmake .. && make && make test;"
            }
        }
    }
}
