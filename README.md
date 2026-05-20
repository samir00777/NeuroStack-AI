NeuroStack-AI/
│
├── frontend/                         # React Frontend
│
│   ├── public/
│   │   └── logo.png
│   │
│   ├── src/
│   │   │
│   │   ├── assets/                  # Images/icons/fonts
│   │   │
│   │   ├── components/              # Reusable UI components
│   │   │   ├── Navbar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── ChatBox.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   ├── Loader.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   │
│   │   ├── pages/                   # Main pages
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── Profile.jsx
│   │   │   └── Admin.jsx
│   │   │
│   │   ├── services/                # API calls
│   │   │   ├── authService.js
│   │   │   ├── chatService.js
│   │   │   └── userService.js
│   │   │
│   │   ├── context/                 # Global state
│   │   │   └── AuthContext.jsx
│   │   │
│   │   ├── routes/
│   │   │   └── AppRoutes.jsx
│   │   │
│   │   ├── utils/
│   │   │   ├── token.js
│   │   │   └── helpers.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
│
├── backend-java/                    # Main Java Backend
│
│   ├── src/
│   │   └── main/
│   │       ├── java/com/neurostack/
│   │       │
│   │       │   ├── config/          # Security/config files
│   │       │   │   ├── JwtConfig.java
│   │       │   │   ├── SecurityConfig.java
│   │       │   │   └── RedisConfig.java
│   │       │   │
│   │       │   ├── controller/      # API endpoints
│   │       │   │   ├── AuthController.java
│   │       │   │   ├── ChatController.java
│   │       │   │   ├── UserController.java
│   │       │   │   └── AdminController.java
│   │       │   │
│   │       │   ├── service/         # Business logic
│   │       │   │   ├── AuthService.java
│   │       │   │   ├── ChatService.java
│   │       │   │   ├── JwtService.java
│   │       │   │   └── UserService.java
│   │       │   │
│   │       │   ├── repository/      # Database queries
│   │       │   │   ├── UserRepository.java
│   │       │   │   └── ChatRepository.java
│   │       │   │
│   │       │   ├── entity/          # Database models
│   │       │   │   ├── User.java
│   │       │   │   ├── Chat.java
│   │       │   │   └── Message.java
│   │       │   │
│   │       │   ├── dto/             # Request/response objects
│   │       │   │   ├── LoginRequest.java
│   │       │   │   ├── RegisterRequest.java
│   │       │   │   └── ChatRequest.java
│   │       │   │
│   │       │   ├── security/
│   │       │   │   ├── JwtFilter.java
│   │       │   │   └── CustomUserDetailsService.java
│   │       │   │
│   │       │   ├── websocket/
│   │       │   │   └── WebSocketConfig.java
│   │       │   │
│   │       │   ├── kafka/
│   │       │   │   ├── KafkaProducer.java
│   │       │   │   └── KafkaConsumer.java
│   │       │   │
│   │       │   ├── exception/
│   │       │   │   └── GlobalExceptionHandler.java
│   │       │   │
│   │       │   └── NeuroStackApplication.java
│   │       │
│   │       └── resources/
│   │           ├── application.properties
│   │           └── static/
│   │
│   ├── Dockerfile
│   ├── pom.xml
│   └── .env
│
│
├── ai-service/                      # Python AI Backend
│
│   ├── app/
│   │   ├── routes/
│   │   │   └── ai_routes.py
│   │   │
│   │   ├── services/
│   │   │   ├── openai_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── pdf_service.py
│   │   │
│   │   ├── models/
│   │   │   └── request_model.py
│   │   │
│   │   ├── utils/
│   │   │   └── tokenizer.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
│
├── docker-compose.yml               # Run all services together
│
├── nginx/                           # Reverse proxy
│   └── nginx.conf
│
├── kubernetes/                      # K8 deployment files
│   ├── frontend.yaml
│   ├── backend.yaml
│   ├── ai-service.yaml
│   └── postgres.yaml
│
├── docs/                            # Documentation
│   ├── API_DOCS.md
│   ├── ARCHITECTURE.md
│   └── DATABASE_SCHEMA.md
│
├── .gitignore
├── README.md
└── LICENSE