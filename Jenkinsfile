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

                  sh 'sh docker compose -p ecommerce-microservices ps'

                    curl -fsS http://localhost:5001/products

                    curl -fsS -X POST \
                    http://localhost:5002/orders \
                    -H "Content-Type: application/json" \
                    -d '{"product_id":1,"quantity":2}'
                '''
            }
        }
    }
}
