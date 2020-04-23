from mycroft import MycroftSkill, intent_file_handler


class CreateTask(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('task.create.intent')
    def handle_task_create(self, message):
        self.speak_dialog('task.create')


def create_skill():
    return CreateTask()

