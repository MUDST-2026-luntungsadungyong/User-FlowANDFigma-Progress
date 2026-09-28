pipeline {
    agent any

    environment {
        PLATFORM_NAME = 'Mythix TCG Platform'
    }

    stages {
        stage('Checkout Full Repository') {
            steps {
                echo '=== Checking out Platform Repository ==='
                checkout scm
            }
        }

        stage('Parallel Build & Test') {
            parallel {
                stage('Backend CI') {
                    steps {
                        dir('Code_devops/tcg-store-backend') {
                            echo '=== Running Backend Tests & Verification ==='
                            sh 'chmod +x ./mvnw || true'
                            sh './mvnw clean test'
                        }
                    }
                }
                stage('Frontend CI') {
                    steps {
                        dir('Code_devops/tcg-store-frontend') {
                            echo '=== Running Frontend Tests & Typecheck ==='
                            sh 'npm ci || npm install'
                            sh 'npm run audit'
                            sh 'npm test'
                            sh 'npm run build'
                        }
                    }
                }
            }
        }

        stage('Validate Docker Compose') {
            steps {
                echo '=== Validating Multi-Service Orchestration ==='
                sh 'docker compose config'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "🎉 ${env.PLATFORM_NAME} Full-Stack CI Passed (Build #${env.BUILD_NUMBER})"
        }
        failure {
            echo "⚠️ ${env.PLATFORM_NAME} Full-Stack CI Failed"
        }
    }
}
