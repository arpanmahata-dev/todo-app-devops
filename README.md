# DevOps Todo Application

A full-stack todo application with an automated CI/CD pipeline demonstrating DevOps best practices.

## 🚀 Features

- Flask-based web application
- Docker containerization
- Infrastructure as Code with Terraform
- CI/CD pipeline with GitHub Actions
- Deployed on AWS EC2 (Free Tier)

## 🛠️ Technologies

- **Backend**: Python, Flask
- **Containerization**: Docker
- **IaC**: Terraform
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EC2, VPC, Security Groups)
- **Region**: ap-south-1 (Mumbai)

## 📦 Project Structure
```
.
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Local development setup
├── templates/
│   └── index.html         # Frontend template
├── terraform/
│   └── main.tf            # Infrastructure configuration
└── .github/
    └── workflows/
        └── deploy.yml     # CI/CD pipeline
```

## 🚦 Getting Started

### Local Development
```bash
# Clone repository
git clone https://github.com/arpanmahata-dev/todo-app-devops.git
cd todo-app-devops

# Run with Docker Compose
docker-compose up

# Or run directly with Python
pip install -r requirements.txt
python app.py
```

### Deployment

1. Configure AWS credentials
2. Generate SSH key: `ssh-keygen -t rsa -b 4096`
3. Deploy infrastructure:
```bash
   cd terraform
   terraform init
   terraform apply
```
4. Set up GitHub secrets
5. Push to the main branch to trigger deployment

## 📊 CI/CD Pipeline

The pipeline automatically:
1. Runs tests on every push
2. Builds Docker image on main branch
3. Pushes image to Docker Hub
4. Deploys to an EC2 instance

## 🔗 Live Demo

Access the application at: `http://YOUR_EC2_IP:5000`

## 👨‍💻 Author

Arpan Mahata
- GitHub: [@arpanmahata-dev](https://github.com/arpanmahata-dev)
- LinkedIn: [arpanmahato](https://linkedin.com/in/arpanmahato)
