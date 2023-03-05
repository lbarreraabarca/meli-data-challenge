package com.data.factory.models

import com.data.factory.utils.FieldValidator
class Json extends Serializable {
  var path: String = _

  def this(path: String) = {
    this()
    this.path = path
  }

  def isValid(): Boolean = new FieldValidator().validStringField("path")(this.path)

}
