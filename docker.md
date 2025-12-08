# Docker

1. What is Docker?
    - Docker is a containerisation platform that packages an application and its dependencies into a lightweight container to ensure consistency across environments.


2. What is a container?
    - A container is a lightweight, isolated runtime environment that shares the host OS kernel and runs an application with its dependencies.

3. Docker vs Virtual Machine

| Docker                | Virtual Machine   |
| --------------------- | ----------------- |
| Lightweight           | Heavy             |
| Shares host OS kernel | Has its own OS    |
| Starts in seconds     | Starts in minutes |

4. What is Docker Engine?

    - Docker Engine is the core service that builds, runs, and manages Docker containers.

5. What are Docker images?

    - Docker images are read-only templates used to create containers.

6. What are Docker containers?

    - Containers are running instances of Docker images.

7. What is Docker Hub?

    - Docker Hub is a cloud registry to store and share Docker images.

8. What is a Dockerfile?

    - A Dockerfile is a text file containing instructions to build a Docker image.

9. Common Dockerfile instructions

    - FROM – Base image

    - RUN – Execute commands

    - COPY / ADD – Copy files

    - CMD – Default command

    - ENTRYPOINT – Fixed startup command

    - EXPOSE – Declare port

10. Difference between CMD and ENTRYPOINT

    - CMD → Can be overridden

    - ENTRYPOINT → Cannot be overridden easily

11. What is a Docker volume?

    - A Docker volume is used for persistent data storage outside containers.

13. What is Docker Compose?

    - Docker Compose is a tool to define and run multi-container applications using docker-compose.yml.


14. Benefits of Docker Compose

    - Multi-container management

    - Single command startup

    - Environment isolation

15. What is docker-compose.yml?

    - A YAML file defining services, networks, volumes, and configurations.

17. Types of Docker networks

    - Bridge

    - Host

    - Overlay

    - None

18. Default Docker network

    - Bridge network.

19. What is port mapping?

    - It maps a container port to a host port.
    ```json
        -p 8000:80
    ```

20. What is EXPOSE used for?

    - It documents the port the container listens on; it does NOT publish the port.

21. What is a multi-stage build?

    - A technique to reduce image size by using multiple FROM stages.

22. Why use multi-stage builds?

    - Smaller images

    - Better security

    - Faster deployments

23. What is a Docker daemon?

    - A background service that manages Docker objects like images, containers, and networks.

24. How do you check running containers?    

    ```json
        docker ps
    ```

25. How do you stop a container?

    ```json
        docker stop <container_id/name>
    ```

26. How do you remove containers and images?

    ```
        docker rm <id>
        docker rmi <image>
    ```

27. What is docker exec?

    It runs commands inside a running container.

    ```python
        docker exec -it container bash
    ```

28. What is docker logs?

    Used to view container logs.
    ```python
        docker logs container
    ```

29. What is docker inspect?

    - Returns detailed container or image information in JSON format.

30. Docker image vs container
| Image     | Container        |
| --------- | ---------------- |
| Blueprint | Running instance |
| Immutable | Mutable          |

31. What is a dangling image?

    - An unused image without a tag.

32. How to clean Docker system?

    ```python
        docker system prune
    ```

33. What is .dockerignore?

    - A file that prevents unwanted files from being copied into the image.

34. What is Docker caching?

    - Docker reuses unchanged image layers to speed up builds.

35. Best practices for Dockerfile

    - Use small base images

    - Minimise layers

    - Use .dockerignore

    - Avoid root user

36. What is Docker Swarm?

    - Docker’s native container orchestration tool.

37. Swarm vs Kubernetes

| Swarm         | Kubernetes        |
| ------------- | ----------------- |
| Simple        | Complex           |
| Docker native | Industry standard |

38. What is a registry?

    - A place to store Docker images (e.g., Docker Hub, AWS ECR).

39. What happens when a container crashes?

    - The container stops unless restart policy is configured.

40. Restart policies

    - no

    - always

    - unless-stopped

    - on-failure

41. What is container isolation?

    - Containers isolate processes using namespaces and cgroups.

42. How does Docker improve CI/CD?

    - Consistent builds

    - Faster testing

    - Easy rollbacks

43. Can containers communicate with each other?

    - Yes, using Docker networks.

44. Difference between ADD and COPY

    - COPY → Simple file copy

    - ADD → Supports URL & tar extraction

45. What is a base image?

    - The starting image in a Dockerfile (e.g., python:3.12).

46. What is Alpine Linux?

    - A lightweight Linux distribution used to create small Docker images.

47. Docker security best practices

    - Use minimal images

    - Non-root users

    - Scan images

48. Can Docker run on Windows?

    - Yes, using Docker Desktop with WSL2.

49. Difference between docker run and docker start

    - run → Creates + starts

    - start → Starts existing container

50. Why is Docker important?

    - It ensures consistency, portability, scalability, and faster deployment.