pipeline {

    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking project source code'
                checkout scm
            }
        }

        stage('Validate') {
            steps {
                echo 'Validating Python files'

                sh '''
                    python3 -m py_compile \
                    product-service/app.py \
                    order-service/app.py \
                    payment-service/app.py
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building all microservices'

               sh 'docker compose -p ecommerce-microservices build'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying microservices'

               sh 'docker compose -p ecommerce-microservices up -d --build'
            }
        }

       stage('Verify Deployment') {
    steps {
        echo 'Checking running containers'
        sh 'docker compose -p ecommerce-microservices ps'

        echo 'Testing Product Service'
        sh 'curl -fsS http://localhost:5001/products'

        echo 'Testing Order Service'
        sh 'curl -fsS http://localhost:5002/orders'
        echo 'Testing Payment Service'
        sh 'curl -fsS http://localhost:5003/payments'
   
    }
}
