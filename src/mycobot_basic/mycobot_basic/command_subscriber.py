import rclpy
from rclpy.node import Node
from mycobot_interfaces.msg import RobotCommand

class CommandSubscriber(Node):
    def __init__(self):
        super().__init__('command_subscriber')
        # Подписываемся на топик /robot_command
        self.subscription = self.create_subscription(
            RobotCommand,
            '/robot_command',
            self.listener_callback,
            10)
        self.subscription  # предотвращает предупреждение о неиспользуемой переменной

    def listener_callback(self, msg):
        # Выводим полученные данные
        self.get_logger().info(f'I heard: command="{msg.command}", speed={msg.speed}, angles={msg.joint_angles}')
        
        # Проверка условия из задания
        if not msg.enable:
            self.get_logger().warn('Command disabled')

def main(args=None):
    rclpy.init(args=args)
    node = CommandSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()