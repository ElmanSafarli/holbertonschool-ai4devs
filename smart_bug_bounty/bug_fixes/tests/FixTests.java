/** Dependency-free Java regressions; explicit checks do not require -ea. */
class FixTests {
    private static int passed = 0;

    private static void check(boolean condition, String name) {
        if (!condition) {
            throw new AssertionError(name);
        }
        passed++;
        System.out.println("PASS: " + name);
    }

    public static void main(String[] args) {
        check(Bug3Fixed.average(new int[]{1, 2}) == 1.5, "bug3 fractional mean");
        check(Bug3Fixed.average(new int[]{-1, -2}) == -1.5, "bug3 negative mean");
        check(Bug3Fixed.average(new int[]{7}) == 7.0, "bug3 single value");
        check(Bug3Fixed.average(new int[]{1, -1}) == 0.0, "bug3 zero mean");
        check(Bug3Fixed.average(new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE})
            == (double) Integer.MAX_VALUE, "bug3 long accumulator");
        boolean rejected = false;
        try {
            Bug3Fixed.average(new int[]{});
        } catch (IllegalArgumentException expected) {
            rejected = true;
        }
        check(rejected, "bug3 rejects empty array");
        check(Bug6Fixed.isAdmin("admin"), "bug6 literal admin");
        check(Bug6Fixed.isAdmin(new String(new char[]{'a', 'd', 'm', 'i', 'n'})),
            "bug6 allocated admin");
        check(!Bug6Fixed.isAdmin("viewer"), "bug6 viewer");
        check(!Bug6Fixed.isAdmin(null), "bug6 null");
        check(!Bug6Fixed.isAdmin("ADMIN"), "bug6 case sensitive");
        check(!Bug6Fixed.isAdmin(""), "bug6 empty string");
        System.out.println("Java checks passed: " + passed);
    }
}
