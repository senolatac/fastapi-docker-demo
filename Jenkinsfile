node('aws_ec2_demo_label') {
    stage 'Checkout'
        checkout scm

    stage 'Build'
        configFileProvider([configFile(fileId: 'demo.env', variable: 'npm_config_registry')]) {
                    sh "cat ${env.npm_config_registry} > prod.env"
        }
        sh 'sudo docker build -t senolatac/demo-ec2-docker-swarm:latest -f Dockerfile .'
        sh 'sudo docker push senolatac/demo-ec2-docker-swarm:latest'

    stage 'Deploy'
        try {
            sh "sudo docker service update --force --image senolatac/demo-ec2-docker-swarm:latest senol-demo"
        } catch (err) {
            sh "sudo docker stack deploy --compose-file docker-compose.yml senol-demo"
        }
}
