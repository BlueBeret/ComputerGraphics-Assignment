
import javax.swing.JPanel;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.awt.Font;
import java.util.Random;
// SOFIRUL DANATRIYA (20/455453/PA/19668)

public class AffineTree extends JPanel {
    // init buffered image dan Graphics
    private BufferedImage img;
    private Graphics g2;
    private int xv, yv, xvmin, yvmin, xvmax, yvmax;
    private double xw, yw, xwmin, ywmin, xwmax, ywmax;
    private Raster pixelArray;
    int[] rgb = new int[3];

    // constructor
    public AffineTree(int[] viewport, double[] window) {
        // buat ukuran sama dengan window
        img = new BufferedImage(Window.WIDTH, Window.HEIGHT, BufferedImage.TYPE_INT_RGB);
        g2 = img.getGraphics();
        xvmin = viewport[0];
        xvmax = viewport[1];
        yvmin = viewport[2];
        yvmax = viewport[3];
        xwmin = window[0];
        xwmax = window[1];
        ywmin = window[2];
        ywmax = window[3];
    }

    public void nama() {
        Font font = new Font("Serif", Font.BOLD, 12);
        g2.setFont(font);
        g2.drawString("Sofirul Danatriya 20/455453/PA/19668", 0, 20);
    }

    private void customDot(int x, int y, Color color, int type, int k) {
        pixelArray.getPixel(x, y, rgb);
        Color colorPix = new Color(rgb[0], rgb[1], rgb[2]);

        // 0 pohon normal
        // 1 pohon musim gugur vs musim semi
        // 2 pohon penyakitan
        // 3 pohon blaster
        // 4 pohon glitch
        // 5 pohon pelangi
        // 6 pohon kah pohon?

        switch (type) {
            case 0:
                if (k > 2) {
                    int r = 0;
                    int g = y * 255 / (yvmax - yvmin);
                    int b = 0;
                    color = new Color(r, g, b);
                }
                break;
            case 1:
                if (k > 2) {
                    int r = x * 255 / (xvmax - xvmin);
                    int g = y * 255 / (yvmax - yvmin);
                    int b = 0;

                    if (((xvmax-xvmin) / 2) + xvmin > x) {
                        r = 10;
                    }
                    color = new Color(r, g, b);
                }
                break;
            case 2:
                if (k > 2) {
                    int r = 0;
                    int g = y * 255 / (yvmax - yvmin);
                    int b = 0;
                    if (x % 8 < 4 && y % 8 < 4) {
                        Random random = new Random();
                        if (random.nextInt(5) == 0) r = 255;
                    }
                    color = new Color(r, g, b);
                }
                break;
            case 3:
                if (k > 2) {
                    int r = 0;
                    int g = y * 255 / (yvmax - yvmin);;
                    int b = 0;
                    if (x % 8 < 4) {
                        r = 255;
                        g = 0;
                    }
                    color = new Color(r, g, b);
                }
                break;
            case 4:
                if (k > 2) {
                    Random random = new Random();
                    int r = random.nextInt(256);
                    int g = random.nextInt(256);
                    int b = random.nextInt(256);
                    color = new Color(r, g, b);
                }
                break;
            case 5:
                if (k > 2) {
                    int r = x * 255 / (xvmax - xvmin);
                    int g = y * 255 / (yvmax - yvmin);
                    int b = (x*x + y*y) % 255;
                    color = new Color(r, g, b);
                }
                break;
            case 6:
                if (k > 2) {
                    int r = x * 255 /( xvmax - xvmin);
                    int g = y * 255 / (yvmax - yvmin);
                    int b = (int) Math.abs(((Math.sin(x * Math.PI/180) + Math.sin(y * Math.PI/180) * 255)))/2 ;
                    color = new Color(r, g, b);
                }
                break;
            default:
            g2.setColor(color);
        }

        if (colorPix.equals(Color.WHITE)) {
            
            g2.setColor(color);
            g2.drawLine(x, y, x, y);
        }
        
    }

    public void drawTree(int alpha, int beta, int gama, Color color, int type ) {
        double xb, yb,
                a0, a1, a2, a3, a4,
                b0, b1, b2, b3, b4,
                c0, c1, c2, c3, c4,
                d0, d1, d2, d3, d4,
                e0, e1, e2, e3, e4,
                f0, f1, f2, f3, f4;

        // rumus affine
        // tengah
        a0 = 0.5 * Math.cos(alpha * Math.PI / 180);
        b0 = -0.5 * Math.sin(alpha * Math.PI / 180);
        c0 = 0.65 * Math.sin(alpha * Math.PI / 180);
        d0 = 0.65 * Math.cos(alpha * Math.PI / 180);
        e0 = -0.02;
        f0 = 1.5;
        // daun kanan 1
        a2 = 0.6 * Math.cos(gama * Math.PI / 180);
        b2 = -0.6 * Math.sin(gama * Math.PI / 180);
        c2 = 0.6 * Math.sin(gama * Math.PI / 180);
        d2 = 0.6 * Math.cos(gama * Math.PI / 180);
        e2 = 0;
        f2 = 2.3;
        // doun kiri 2
        a1 = 0.65 * Math.cos(-gama * Math.PI / 180);
        b1 = -0.65 * Math.sin(-gama * Math.PI / 180);
        c1 = 0.6 * Math.sin(-gama * Math.PI / 180);
        d1 = 0.6 * Math.cos(-gama * Math.PI / 180);
        e1 = 0;
        f1 = 2.0;
        // daun 3 kanan
        a3 = 0.65 * Math.cos(beta * Math.PI / 180);
        b3 = -0.65 * Math.sin(beta * Math.PI / 180);
        c3 = 0.6 * Math.sin(beta * Math.PI / 180);
        d3 = 0.6 * Math.cos(beta * Math.PI / 180);
        e3 = 0;
        f3 = 1.6;
        // daun 4 kiri
        a4 = 0.65 * Math.cos(-beta * Math.PI / 180);
        b4 = -0.65 * Math.sin(-beta * Math.PI / 180);
        c4 = 0.6 * Math.sin(-beta * Math.PI / 180);
        d4 = 0.6 * Math.cos(-beta * Math.PI / 180);
        e4 = 0;
        f4 = 1.3;

        // buat background jadi putih
        g2.setColor(Color.white);
        g2.fillRect(xvmin, yvmin, xvmax, yvmax);

        // buat batang pohon pertama
        int[] objekX = { xvmax / 2 + 7, xvmax / 2 - 7, xvmax / 2 - 5, xvmax / 2 + 5 };
        int[] objekY = { yvmax, yvmax, 430, 430 };

        g2.setColor(new Color(100, 70, 36));
        
        g2.fillPolygon(objekX, objekY, 4);

        // raster untuk mendapat warna pixel
        
        // banyak iterasi
        int numit = 8, k = 1;
        while (k < numit) {
            pixelArray = img.getData();
            for (int i = xvmin; i < xvmax; i++) {
                for (int j = yvmin; j < yvmax; j++) {
                    // cek warna pixel
                    pixelArray.getPixel(i, j, rgb);
                    // buat objek warna
                    Color colorPix = new Color(rgb[0], rgb[1], rgb[2]);
                    if (!colorPix.equals(Color.white)) {
                        
                        // jika bukan putih maka ada objek
                        // ubah dari viewport ke world
                        v2w(i, j);
                        // gambar objek tengah
                        xb = a0 * xw + b0 * yw + e0;
                        yb = c0 * xw + d0 * yw + f0;
                        w2v(xb, yb);
                        customDot(xv, yv, color, type, k);
                        // gambar daun pertama kanan
                        xb = a1 * xw + b1 * yw + e1;
                        yb = c1 * xw + d1 * yw + f1;
                        w2v(xb, yb);
                        customDot(xv, yv, color, type, k);
                        // gambar daun pertama kiri
                        xb = a2 * xw + b2 * yw + e2;
                        yb = c2 * xw + d2 * yw + f2;
                        w2v(xb, yb);
                        customDot(xv, yv, color, type, k);
                        // gambar daun ketiga kanan
                        xb = a3 * xw + b3 * yw + e3;
                        yb = c3 * xw + d3 * yw + f3;
                        w2v(xb, yb);
                        customDot(xv, yv, color, type, k);
                        // gambar daun ke 4 kanan
                        xb = a4 * xw + b4 * yw + e4;
                        yb = c4 * xw + d4 * yw + f4;
                        w2v(xb, yb);
                        customDot(xv, yv, color, type, k);
                    }
                }
            }
            k++;
        }
    }

    public Color getRandomColor() {
        Random random = new Random();
        int red = random.nextInt(255);
        int green = random.nextInt(255);
        int blue = random.nextInt(255);
        return new Color(red, green, blue);
    }

    public void paintComponent(Graphics g) {
        g.drawImage(img, 0, 0, null);
    }

    // fungsi transformasi window ke viewport dan sebaliknya
    public void w2v(double xw, double yw) {
        xv = xvmin + (int) Math.round((xw - xwmin) * (xvmax - xvmin) / (xwmax - xwmin));
        yv = yvmax - (int) Math.round((yw - ywmin) * (yvmax - yvmin) / (ywmax - ywmin));
    }

    public void v2w(int xv, int yv) {
        xw = xwmin + (xv - xvmin) * (xwmax - xwmin) / (xvmax - xvmin);
        yw = ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin);
    }
}
