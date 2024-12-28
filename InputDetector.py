import pyxel

class InputDetector():
  # 上方向の入力
  UP = [
    pyxel.KEY_UP,
    pyxel.GAMEPAD1_BUTTON_DPAD_UP,
    pyxel.KEY_W,
  ]

  # 下方向の入力
  DOWN = [
    pyxel.KEY_DOWN,
    pyxel.GAMEPAD1_BUTTON_DPAD_DOWN,
    pyxel.KEY_S,
  ]

  # 左方向の入力
  LEFT = [
    pyxel.KEY_LEFT,
    pyxel.GAMEPAD1_BUTTON_DPAD_LEFT,
    pyxel.KEY_A,
  ]

  # 右方向の入力
  RIGHT = [
    pyxel.KEY_RIGHT,
    pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT,
    pyxel.KEY_D,
  ]

  # 上で定義した配列を代入し、その中に該当する入力があればTrueを返す
  def is_pressed(key:list[int]) -> bool:
    for k in key:
      if pyxel.btn(k):
        return True
    return False

  #こちらはキーを離した場合のための関数
  def is_released(key:list[int]) -> bool:
    for k in key:
      if pyxel.btnr(k):
        return True
    return False