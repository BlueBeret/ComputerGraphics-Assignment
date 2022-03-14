
import java.awt.*;
import java.awt.geom.Ellipse2D;
import javax.swing.*;

public class App extends JPanel {


    public static void main(String[] args) throws Exception {
        App panel = new App();
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1920, 1080);
        frame.getContentPane().add(panel);
        frame.setVisible(true);
    }

    public void garisLurus(int x1, int y1, int x2, int y2){
        System.out.println("Garis Lurus");
    }

    public void titik(Graphics g) {
        Graphics2D t2k = (Graphics2D) g;
        t2k.setColor(Color.RED);
        t2k.drawLine(960, 550, 960, 550);
        t2k.drawLine(961, 550, 961, 550);
        t2k.drawLine(960, 551, 960, 551);
        t2k.drawLine(961, 551, 961, 551);
    }

}
