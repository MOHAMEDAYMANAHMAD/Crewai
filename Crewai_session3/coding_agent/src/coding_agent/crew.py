from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

@CrewBase
class CodingAgent():
    """CodingAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[search_tool]
        )

    @agent
    def write_report(self) -> Agent:
        return Agent(
            config=self.agents_config['write_report'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def vali_info(self) -> Agent:
        return Agent(
            config=self.agents_config['vali_info'], # type: ignore[index]
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )
    
    @task
    def write_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_report_task'], # type: ignore[index]
        )
    
    @task
    def vali_info_task(self) -> Task:
        return Task(
            config=self.tasks_config['vali_info_task'], # type: ignore[index]
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CodingAgent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
