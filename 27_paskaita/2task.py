from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///second_task.db")
Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    deadline = Column(String)
    tasks = relationship("Task", back_populates="project")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    description = Column(String)
    status = Column(String)
    project = relationship("Project", back_populates="tasks")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


projects = [
    Project(name="Project A", deadline="2025-06-01"),
    Project(name="Project B", deadline="2025-07-15"),
    Project(name="Project C", deadline="2025-08-20"),
    Project(name="Project D", deadline="2025-09-10"),
    Project(name="Project E", deadline="2025-10-05"),
]

# session.add_all(projects)
session.commit()

statuses = ["Pending", "In Progress", "Completed"]
for project in session.query(Project).all():
    for i, status in enumerate(statuses):
        session.add(Task(project_id=project.id, description=f"Task {i+1} for {project.name}", status=status))
session.commit()


project_id = 1
tasks = session.query(Task).filter(Task.project_id == project_id).all()
print(f"Tasks for Project ID {project_id}:")
for task in tasks:
    print(task.description, "-", task.status)

incomplete_projects = session.query(Project).join(Task).filter(Task.status != "Completed").distinct().all()
print("\nProjects with incomplete tasks:")
for project in incomplete_projects:
    print(project.name)







