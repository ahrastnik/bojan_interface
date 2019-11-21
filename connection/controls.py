
class BojanControls:
    COMMAND_JOG = "J "
    COMMAND_WORK_MOVE = "G1"
    COMMAND_FAST_MOVE = "G0"

    def __init__(self):
        pass

    def jog(self, dir, vel):
        x_dir = dir[0] * vel
        y_dir = dir[1] * vel

        X = "X" + str(x_dir)
        Y = "Y" + str(y_dir)

        gCode = self.COMMAND_JOG + X + " " + Y

        return gCode

if __name__ == '__main__':
    controls = BojanControls()

    gCode = controls.jog([10,2], 20)
    print(gCode)