import rclpy
from rclpy.node import Node
from mycobot_interfaces.msg import RobotCommand
import math

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        # Создаем издателя в топик /robot_command
        self.publisher_ = self.create_publisher(RobotCommand, '/robot_command', 10)
        # Таймер на 1 Гц (раз в секунду)
        timer_period = 1.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = RobotCommand()
        msg.command = "move_to_pose"
        
        # Синусоидальное изменение углов (как рекомендуется в задании)
        # Заполняем массив 6 значениями
        angle = math.sin(self.i * 0.1) 
        msg.joint_angles = [angle, -angle, angle, 0.0, 0.0, 0.0] 
        
        msg.speed = 0.5
        msg.enable = True  # Поставь False, чтобы проверить работу предупреждения в подписчике
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: command="{msg.command}", speed={msg.speed}, angles[0]={msg.joint_angles[0]:.2f}')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()