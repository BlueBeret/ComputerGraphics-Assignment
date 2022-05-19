
import javax.swing.JFrame;
import java.awt.Color;
import java.util.Scanner;

public class Window {
	// Ukuran window
	public static final int WIDTH = 500;
	public static final int HEIGHT = 625;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		// 0 pohon normal
        // 1 pohon musim gugur vs musim semi
        // 2 pohon penyakitan
        // 3 pohon blaster
        // 4 pohon glitch
        // 5 pohon pelangi
		// 6 pohon kah pohon?
		System.out.println("0. Normal\n1. Musim gugur vs musim semi\n2. Penyakitan\n3. Blaster\n4. Glitch\n5. Pelangi\n6. Kah pohon?");
		System.out.print("Pilih pohon: ");
		int type = scanner.nextInt();
		scanner.close();

		// buat object window dan panel
		JFrame myWindow = new JFrame("Default Window");
		AffineTree myPanel = new AffineTree(new int[] { 0, 500, 0, 625 }, new double[] { -3, 3, 0, 7.5 });

		// tambah panel ke window dan gambar affine
		myWindow.add(myPanel);
		myPanel.drawTree(0, -20, 20, new Color(100, 70, 36), type);
		myPanel.nama();
		myWindow.pack();

		// inisialisasi ukuran window dan disable resizable
		myWindow.setSize(WIDTH, HEIGHT);
		myWindow.setResizable(false);
		myWindow.setLocationRelativeTo(null);
		myWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		myWindow.setVisible(true);
	}
}
