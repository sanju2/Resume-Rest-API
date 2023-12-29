import json

def lambda_handler(event, context):
    json_data = [{
        "basics": {
            "name": "Lasantha Sanjeewa Silva",
            "label": "DevOps/Cloud Engineer",
            "picture": "",
            "email": "lsanjeewa947@gmail.com",
            "phone": "(971) 553781902",
            "website": "https://devopswithlasantha.tech",
            "summary": "Cloud & DevOps Enthusiast, AWS Community Builder",
            "location": {
                "address": "Al Nahda2,Dubai,UAE",
                "city": "Dubai"
            },
            "profiles": [{
                "network": "Twitter",
                "username": "@LasanthaSilva96",
                "url": "https://twitter.com/LasanthaSilva96"
            },
                {
                "network": "Linkedin",
                "username": "Lasantha Sanjeewa Silva",
                "url": "https://www.linkedin.com/in/lasanthasilva/"
            },
                {
                "network": "GitHub",
                "username": "sanju2",
                "url": "https://github.com/sanju2"
            }]
        },
        "work": [{
            "company": "Toshiba Elevator Middle East LLC",
            "position": "Information Technology Assistant",
            "startDate": "2022-08-22",
            "endDate": "Present",
            "summary": "Azure, Active Directory, Windows OS, MS365, Networking",
        }, {
            "company": "Calcey Technologies",
            "position": "Associate DevOps Engineer",
            "startDate": "2021-09-21",
            "endDate": "2022-03-31",
            "summary": "Work with AWS & CI/CD",
        }, {
            "company": "LOLC Technologies Ltd",
            "position": "Cloud & DevOps Intern",
            "startDate": "2021-01-06",
            "endDate": "2021-07-05",
            "summary": "Work with OCI,GCP & CI/CD",
        }],
        "education": [{
            "institution": "Uva Wellassa University of SriLanka",
            "area": "Computer Science",
            "studyType": "Master Degree - Reading",
            "startDate": "2023-07-29",
            "endDate": "Present",
        },{
            "institution": "Uva Wellassa University of SriLanka",
            "area": "Computer Science",
            "studyType": "Bachelor Degree",
            "startDate": "2017-01-21",
            "endDate": "2022-03-31",
        }],
        "Extra-Curricular-Activities": [{
            "title": "AWS Community Builder",
            "date": "2022-03-05",
            "awarder": "AWS",
        },
            {
            "title": "Postman Student Expert",
            "date": "2022-04-11",
            "awarder": "Postman",
        }
        ],
        "skills": [
            {
                "name": "AWS",
                "level": "Intermediate",
                "keywords": [
                    "DevOps",
                    "Lambda",
                    "EC2",
                    "S3",
                    "EKS"
                ]
            },
            {
                "name": "Azure",
                "level": "Intermediate",
                "keywords": [
                    "Azure VM",
                    "Azure AD",
                    "Storage",
                    "Azure DevOps"
                ]
            },
            {
                "name": "Terraform",
                "level": "Intermediate",
                "keywords": [
                    "IaC"
                ]
            },
            {
                "name": "Docker",
                "level": "Intermediate",
                "keywords": [
                    "Containers",
                    "Docker-Compose"
                ]
            }
        ],
        "interests": [{
            "name": "Tech Blogging",
            "keywords": [
                "Article Writing",
                "DevOps, DevSecOps, Cloud & AWS"
            ]
        }]
    }]

    json_str = json.dumps(json_data, indent=4)

    return {'statusCode': 200,
            'body': json_str
            }