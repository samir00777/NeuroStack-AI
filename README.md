Folder PATH listing for volume Windows-SSD
Volume serial number is B6C9-4081
C:.
|   docker-compose.yml
|   LICENSE
|   NeuroStack-AI.gitignore
|   README.md
|   structure.txt
|   
+---ai-service
|   |   .env
|   |   Dockerfile
|   |   requirements.txt
|   |   
|   \---app
|       |   main.py
|       |   
|       +---models
|       |       request_model.py
|       |       
|       +---routes
|       |       ai_routes.py
|       |       
|       +---services
|       |       embedding_service.py
|       |       openai_service.py
|       |       pdf_service.py
|       |       
|       \---utils
|               tokenizer.py
|               
+---backend-java
|   |   .env
|   |   Dockerfile
|   |   pom.xml
|   |   
|   +---src
|   |   \---main
|   |       +---java
|   |       |   \---com
|   |       |       \---neurostack
|   |       |           |   NeuroStackApplication.java
|   |       |           |   
|   |       |           +---config
|   |       |           |       SecurityConfig.java
|   |       |           |       
|   |       |           +---controller
|   |       |           |       AdminController.java
|   |       |           |       AuthController.java
|   |       |           |       ChatController.java
|   |       |           |       UserController.java
|   |       |           |       
|   |       |           +---dto
|   |       |           |       LoginRequest.java
|   |       |           |       
|   |       |           +---entity
|   |       |           |       User.java
|   |       |           |       
|   |       |           +---exception
|   |       |           |       GlobalExceptionHandler.java
|   |       |           |       
|   |       |           +---kafka
|   |       |           +---repository
|   |       |           |       UserRepository.java
|   |       |           |       
|   |       |           +---security
|   |       |           +---service
|   |       |           |       AuthService.java
|   |       |           |       ChatService.java
|   |       |           |       JwtService.java
|   |       |           |       UserService.java
|   |       |           |       
|   |       |           \---websocket
|   |       \---resources
|   |           |   application.properties
|   |           |   
|   |           \---static
|   \---target
|       |   neurostack-backend-0.0.1-SNAPSHOT.jar
|       |   
|       +---classes
|       |   |   application.properties
|       |   |   
|       |   \---com
|       |       \---neurostack
|       |           |   NeuroStackApplication.class
|       |           |   
|       |           +---config
|       |           |       SecurityConfig.class
|       |           |       
|       |           +---controller
|       |           |       AdminController.class
|       |           |       AuthController.class
|       |           |       ChatController.class
|       |           |       UserController.class
|       |           |       
|       |           +---dto
|       |           |       LoginRequest.class
|       |           |       
|       |           +---entity
|       |           |       User.class
|       |           |       
|       |           +---exception
|       |           |       GlobalExceptionHandler.class
|       |           |       
|       |           +---repository
|       |           |       UserRepository.class
|       |           |       
|       |           \---service
|       |                   AuthService.class
|       |                   ChatService.class
|       |                   JwtService.class
|       |                   UserService.class
|       |                   
|       +---generated-sources
|       |   \---annotations
|       +---maven-archiver
|       |       pom.properties
|       |       
|       \---maven-status
|           \---maven-compiler-plugin
|               \---compile
|                   \---default-compile
|                           createdFiles.lst
|                           inputFiles.lst
|                           
+---docs
|       API_DOCS.md
|       ARCHITECTURE.md
|       DATABASE_SCHEMA.md
|       
+---frontend
|   |   package.json
|   |   vite.config.js
|   |   
|   +---public
|   |       logo.png
|   |       
|   \---src
|       |   App.jsx
|       |   index.css
|       |   main.jsx
|       |   
|       +---assets
|       +---components
|       |       ChatBox.jsx
|       |       Loader.jsx
|       |       MessageBubble.jsx
|       |       Navbar.jsx
|       |       ProtectedRoute.jsx
|       |       Sidebar.jsx
|       |       
|       +---context
|       |       AuthContext.jsx
|       |       
|       +---pages
|       |       Admin.jsx
|       |       Chat.jsx
|       |       Dashboard.jsx
|       |       Home.jsx
|       |       Login.jsx
|       |       Profile.jsx
|       |       Register.jsx
|       |       
|       +---routes
|       |       AppRoutes.jsx
|       |       
|       +---services
|       |       authService.js
|       |       chatService.js
|       |       userService.js
|       |       
|       \---utils
|               helpers.js
|               token.js
|               
+---kubernetes
|       ai-service.yaml
|       backend.yaml
|       frontend.yaml
|       postgres.yaml
|       
\---nginx
        nginx.conf
        
