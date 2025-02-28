Star Wars API Starships and Pilots Information
A brief explanation of your approach:
    This project retrieves and displays information about starships and pilots from the Star Wars API (SWAPI). It includes details such as name, model, crew, passengers, starship class, and more for each starship. Each pilot has information for their name, height, mass, hair color, and more printed to the console. The project also collects unique URLs for pilots and films, among others, associated with the starships and pilots.

Step-by-step instructions on how to pull the Docker image and run the container:
User Instructions, Accessing GHCR Image:
    1. Open Docker Desktop on your computer or download it if you haven't already.
     Docker needs to be running in order to download the Docker image and run the container.
    2. Run this command in the terminal to download the Docker image from GHCR
    docker pull ghcr.io/willg08/devops/starwars-api:latest
    3. Run this command in the terminal to run the Docker container on GHCR
    docker run --rm ghcr.io/willg08/devops/starwars-api:latest

Host Instructions, Building your own Docker Image:
    1. Build the Docker image locally
    docker build -t ghcr.io/willg08/devops/starwars-api:latest .

    2. Verify the image is built
    docker images

    3. Login to Docker, user Personal Access Token for github token
    docker login ghcr.io -u <github username> -p <your_github_token>

    4. Push the Docker Image to GHCR
    docker push ghcr.io/willg08/devops/starwars-api:latest

    5. Run this command in the terminal to pull the Docker project from GHCR
    docker pull ghcr.io/willg08/devops/starwars-api:latest

    6. Run this command in the terminal to run the Docker project
    docker run --rm ghcr.io/willg08/devops/starwars-api:latest


Any additional notes on assumptions or design choices.
    Assumptions:
    The project assumes that the Star Wars API (SWAPI) is available and reliable throughout the execution. This includes assuming that the API will return consistent data in the expected format (JSON). There is a method to catch errors with the api retrieving information, but without that API there isn't any use to the project so far. As of now we assume the API will provide valid data for starships and pilots, such as names, models, crew size, etc., without unexpected errors or missing fields. A potential issue of the project would be if the project has an API request rate limiting or blocking. If rate limits were encountered, the program would need further handling for these situations. We have an assumption that the data returned by the API is always structured in the same format, particularly with fields like results, next, and nested lists such as pilots and films. 
    
    Design Choices:
    This project is hosted on GHCR so it can be ran on any computer with Docker by running two commands, pull and run. One nice feature is the get_data_from_api() method. This method uses a retry mechanism in case of timeouts when fetching data from the API. The get_data_from_api function will retry up to three times if it encounters a timeout, with a 5-second wait between retries. This is designed to handle potential network issues or temporary API unavailability. It will also display an error message if the status code is not valid. Sets are used to store unique pilot URLs, film URLs, species URLs, vehicle URLs, and starship URLs. These sets are now ready for further manipulation without redundant references to pilots, films, or another category. By using a set, you ensure that each pilot and film URL is listed only once, regardless of how many times they appear in different starships. The code uses a while loop to handle pagination by continuously fetching data from the API until there is no next page. This design is chosen to ensure that the program can handle potentially large amounts of data without overwhelming the user or running into memory issues. The project separates the retrieval and display of starship and pilot information, allowing for clarity in code structure and better organization. The starships_url retrieves data about starships, and unique pilots are collected and processed separately. The program prints a limited amount of information for both starships and pilots, primarily focusing on key attributes like name, model, crew, height, and gender. Some attributes are commented out to avoid unnecessary complexity and clutter in the output, but they could easily be added if needed. The formatted sets are also printed out at the bottom of the output to be out of the way but clear that they are properly formatted for further use. The code is structured in a way that it can be easily extended to include additional information, such as other API keys or attributes of starships and pilots, without requiring a major redesign. There are also clear headers to separate sections in the code and output for easy viewing. The outputted counters next to both the starships and pilots for organization are used for quickly checking the amount of starships and pilots 

A section discussing production deployment considerations
1.Container Orchestration & Scaling:
    1.1.Deployment using orchestration tools (e.g., Kubernetes, Docker Swarm).
    ANSWER: First we should compare the orchestrations tools to determine the complexity, scale and needs of this project. Kubernetes is a powerful, open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications. It is suitable for more complex or large-scale projects. Docker Swarm is Docker's native container orchestration tool. It's more lightweight and simpler to set up and use than Kubernetes but still provides many useful features for scaling Docker applications. 
    
    Overall, I would choose Docker Swarm for this project due to simplicity, cost-effectiveness, and minimal infrastructure needs. This application doesn’t require the extensive complexity that Kubernetes brings. With Docker Swarm, scaling and management of a few services (such as simple GET requests to the Star Wars API) or other APIs are much easier to handle. There are not a ton of services needed for this project and Docker Swarm provides enough scalability and ease of use without incurring extra costs that Kubernetes would. Unless we change the purpose of this project, add a large amount of services, or get an extremely large amount of volume to the website we should have enough functionality and computing power for Docker Swarm. It is important to keep in mind that while Docker Swarm is sufficient for our current needs, Kubernetes is better for larger scale growth and more complex applications, so this decision should be reevaluated periodically.

    1.2.Strategies for scaling the application (e.g., auto-scaling based on load).
    ANSWER: Docker Swarm provides basic scaling capabilities through replication and load balancing. Docker Swarm allows you to scale the application by increasing or decreasing the number of container instances (replicas) that are running. This can be done manually by running the command docker service scale <service_name>=<replica_count>. For example, if traffic increases, you can add more instances of the API service. Swarm handles load balancing across containers automatically. When a container is created or removed, the load balancer adjusts the traffic distribution, ensuring an even load. Tools like Prometheus and Grafana can send me alerts or automatically trigger scaling actions based on load using external tools/scripts. 
    
    One of the biggest advantages of Kubernetes is Kubernetes can automatically increase or decrease the number of pods (containers) based on CPU usage or custom metrics such as network traffic or latency. For a larger Kubernetes deployment, you could use a Cluster Autoscaler that automatically adjusts the size of your cluster based on resource needs. Kubernetes also supports scaling up individual pods by increasing their resources (CPU and memory) instead of scaling the number of pods. As you can see the scaling process is much more autonomous with the Kubernetes system, but the functionality is probably over the top for what we are looking for on this project. Due to the ease of use, cheaper price, and sufficient functionality is offered for Docker Swarm I believe that is the best choice.

    Price Estimates assuming Low Traffic, less than 100 users a day, 10 to 20 requests per minute for peak traffic
    Docker Swarm:
    AWS: $10 to $20 a month
        EC2 Instance (t3.micro, 1 vCPU, 1 GB RAM): Around $8.47 per month (on-demand pricing).
        Storage (EBS): $0.10 per GB per month (e.g., 10 GB = $1/month).
        Elastic IP (if used): $3.65 per month.
        Data Transfer Costs: Usually around $0.09 per GB, but this can vary.
    Google Cloud: $7 to $15 a month
        F1-micro instance (1 vCPU, 0.6 GB RAM): Around $4.74 per month.
        Persistent Disk Storage: $0.04 per GB per month (e.g., 10 GB = $0.40/month).
        Data Transfer Costs: Similar to AWS, around $0.12 per GB.
    Azure: $10 to $20 a month
        B1s VM (1 vCPU, 1 GB RAM): $7.64/month.
        Storage: $0.08 per GB (e.g., 10 GB = $0.80/month).
        Bandwidth Costs: Around $0.09 per GB.

    Kubernetes:
    AWS: $30 to $50 a month
        EKS Control Plane: $0.10 per hour (approximately $72/month).
        EC2 Instances (t3.micro): Around $8.47/month per instance.
        Storage (EBS): Same as Docker Swarm, around $0.10 per GB/month.
        Data Transfer Costs: $0.09 per GB.
    Google Cloud: $25 to $40 a month
        GKE Cluster Management Fee: $0.10 per hour (approximately $72/month).
        Compute Instances (e2-micro): $5.40/month per instance.
        Persistent Disk Storage: $0.04 per GB (e.g., 10 GB = $0.40/month).
        Data Transfer Costs: $0.12 per GB.
    Azure: $15 to $30 a month
        AKS Control Plane: Free (no charge for the Kubernetes control plane, but you pay for VMs and other resources).
        VM (B1s, 1 vCPU, 1 GB RAM): $7.64/month.
        Storage: $0.08 per GB (e.g., 10 GB = $0.80/month).
        Data Transfer Costs: $0.09 per GB.

2.Monitoring & Logging:
    2.1.Tools and techniques to monitor the application’s health and performance.
    ANSWER: Prometheus is an open-source monitoring tool that collects and stores metrics as time-series data. It works well for tracking metrics like request rates, CPU usage, memory usage, and error rates. Grafana is an open-source visualization tool that can be paired with Prometheus. It allows you to build dashboards to visually monitor metrics in real-time. You can use Prometheus to monitor the performance of the Docker containers, such as CPU usage, memory consumption, request counts, error rates, etc. Grafana helps you visualize these metrics on a dashboard for easy monitoring.

    2.2.Strategies for centralized logging (e.g., ELK Stack, Fluentd).
    ANSWER: Centralized logging is crucial in a production environment because it helps collect, store, and manage logs from multiple services and systems in one place, making it easier to monitor application performance, troubleshoot issues, and ensure security and compliance. In a distributed architecture, such as one using Docker containers or microservices, logs are typically scattered across different machines, making it difficult to track and analyze them. Centralized logging solves this problem by aggregating logs from all sources into a single system for efficient analysis. ELK Stack would be better for this project because you need a complete logging solution where you can collect, store, search, and visualize logs all in one place. This is also helpful for using Prometheus and Grafana to monitor the system's health and performance. Fluentd can be used to collect logs but doesn't offer visualization and search out of the box.

    ELK Stack is a widely used solution for centralized logging using Elasticsearch, Logstash, and Kibana. Elasticsearch allows for quick and complex searches across massive datasets by storing logs, enabling fast log retrieval. This can help with finding errors in the system, speeding up user interactions, better CPU usage, and speeding up system events. Logstash is a data processing pipeline that collects, parses, and transforms log data from various sources and sends it to Elasticsearch for storage. Kibana is a visualization tool that helps to analyze and monitor logs stored in Elasticsearch. It provides dashboards for exploring and understanding log data.
 
3.CI/CD Pipeline:
    3.1.How you would integrate your Docker build process into a CI/CD pipeline.
    Steps for automated testing, security scanning, and deployment.
    ANSWER: To integrate my Docker build into a continuous integration, continuous delivery pipeline, I would use GitHub Actions because I am already using GitHub for version control. GitHub Actions, through on triggers (e.g., when pushing to the main branch), can automatically trigger Docker container and image builds using docker build commands. It can also deploy to Docker Swarm by using Docker commands, such as pushing Docker images to a container registry or deploying them to a Swarm cluster. I can add automated testing steps (unit tests, integration tests) within the workflow, ensuring that any code changes are thoroughly tested before deployment. GitHub Actions can also trigger deployment to a test/staging environment, and even production, using Docker Swarm. GitHub Actions supports integration with Prometheus and Grafana for monitoring and ELK Stack for centralized logging. CodeQL is a code analysis tool that helps identify security vulnerabilities and code quality issues by analyzing source code through custom queries. To deploy CodeQL, you can integrate it into your CI/CD pipeline using GitHub Actions, where it automatically scans your repository for vulnerabilities and generates detailed reports during pull requests or commits. CodeQL is built by GitHub and can be used alongside Dependabot for better results.

4.Security & Reliability:
    4.1.Security considerations (e.g., vulnerability scanning, minimal base images, secrets management).
    ANSWER: For security scanning, I would integrate a Docker image scanning tool such as Trivy within the GitHub Actions workflow. Trivy can scan the Docker images for vulnerabilities, including outdated dependencies, known CVEs (Common Vulnerabilities and Exposures), and insecure configurations, before pushing the images to any registry. This helps to ensure that only secure images are deployed to production. Additionally, I would use Dependabot within GitHub Actions to automatically scan the project’s dependencies for known vulnerabilities. Dependabot can create pull requests to update insecure dependencies as soon as vulnerabilities are discovered, ensuring that the codebase remains up to date and secure. For secrets management, I would use GitHub Secrets to securely store sensitive information such as API keys, database passwords, and other secrets needed by the application. GitHub Actions integrates with GitHub Secrets to safely inject these values into workflows without exposing them in code. We may need a database in the future to save user profiles for the project. To reduce the attack surface, I would also ensure the use of minimal base images for Docker. Using slim images or minimal base images (such as Alpine Linux) helps to reduce the potential vulnerabilities by minimizing the number of packages and dependencies in the image. Finally, I would implement regular security audits, using tools like CodeQL or SonarQube, to continuously check for potential code vulnerabilities, security flaws, or bad practices in the repository and codebase.

    4.2.Ensuring reliability and availability (e.g., health checks, redundancy, fault tolerance).
    ANSWER: For ensuring reliability and availability, I would implement health checks for the Docker containers. Docker’s built-in HEALTHCHECK instruction would be used to periodically test whether each container is running correctly. If a container fails the health check, it can be restarted automatically, ensuring that the application remains available. To improve redundancy, I would deploy the application using Docker Swarm, which allows for easy scaling of containers and ensures that there are multiple instances of the application running across different nodes. This provides failover capabilities, so if one instance fails, others can handle the load. For fault tolerance, I would set up replicas in Docker Swarm, ensuring that there are multiple copies of each service running. This provides high availability and ensures that the application remains operational even if a service or node fails. Additionally, I would integrate auto-scaling to scale the services based on traffic or load. This can be achieved through Docker Swarm’s auto-scaling features or integrating with monitoring tools like Prometheus and Grafana. These tools can provide alerts when the system is under heavy load, triggering the scaling of services to handle increased demand.

5.Configuration Management:
    5.1.Handling configuration settings for different environments (development, staging, production) using environment variables or configuration files.
    ANSWER: Using Docker, environment variables can be passed into the container through the docker-compose.yml file or directly in the Dockerfile. For example, in docker-compose.yml, you can set different values for each environment. For example, variables like API endpoints, database connections, or any environment-specific secrets (e.g., API keys) can be set differently for development, staging, and production environments. In addition to environment variables, configuration files can be used to store non-sensitive, environment-specific settings (like logging levels, API configurations, etc.). These files can be maintained separately for each environment (e.g., config.dev.json, config.prod.json) and placed in the appropriate directories. For instance, for a Python-based project, you could use .env files to store environment-specific configurations, and a library like python-dotenv can help load them. Each environment (development, staging, production) could have a separate .env file that gets loaded accordingly.

6.Document the workflow in your README, explaining the process and benefits of using CI/CD in your workflow.
    Workflow:

