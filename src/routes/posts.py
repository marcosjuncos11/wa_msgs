from flask import Blueprint

posts = Blueprint("posts", __name__)


@posts.route("/", methods=["GET"])
def create_token():
  return 'done!'