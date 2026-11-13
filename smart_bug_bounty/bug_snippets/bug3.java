// Exercise: calculate an arithmetic mean without losing fractions.
class Bug3 {
    static double average(int[] values) {
        if (values.length == 0) {
            throw new IllegalArgumentException("values must not be empty");
        }
        long total = 0;
        for (int value : values) {
            total += value;
        }
        return total / values.length;
    }

    public static void main(String[] args) {
        int[] scores = {1, 2};
        System.out.println(average(scores));
    }
}
