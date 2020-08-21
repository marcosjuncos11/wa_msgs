class AppConfig:
  __conf = {
    "SECRET_KEY": 'guada-lupe-jun-cos-21-05-09'    
  }
  # __setters = ["username", "password"]

  @staticmethod
  def config(name):
    return AppConfig.__conf[name]

  # @staticmethod
  # def set(name, value):
  #   if name in App.__setters:
  #     App.__conf[name] = value
  #   else:
  #     raise NameError("Name not accepted in set() method")