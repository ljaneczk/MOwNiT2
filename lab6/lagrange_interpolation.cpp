#include <iostream>
template <typename T>
T min(T a, T b) { return (a <= b) ? a : b; }
template <typename T>
T max(T a, T b) { return (a >= b) ? a : b; }
#define T double

struct double_pair {
	double fi;
	double se;
};

//template <typename T>
struct poly {
	int n;
	T *a;
	poly(int n) {
		this->n = n;
		this->a = new T[n+1];
		for (int i = 0; i <= n; i++)
			this->a[i] = 0;
	}
	poly() : poly(0) {
	}
	poly(int n, T *a) {
		this->n = n;
		this->a = a;
	}
	poly(int n, T a, T b) : poly(1) {
		this->a[0] = b;
		this->a[1] = a;
	}
	poly operator *(poly other) const {
		poly *that = &other;
		int n1 = this->n + that->n;
		T *c = new T[n1+1];
		for (int i = 0; i <= n1; i++)
			c[i] = 0;
		for (int i = 0; i <= this->n; i++)
			for (int j = 0; j <= that->n; j++)
				c[i+j] += this->a[i] * that->a[j];
		return poly(n1, c);
	}
	poly operator *(T k) const {
		int n1 = this->n;
		T *c = new T[n1+1];
		for (int i = 0; i <= n1; i++)
			c[i] = this->a[i] * k;
		return poly(n1, c);
	}
	poly operator +(poly other) const {
		poly *that = &other;
		int n1 = max(this->n, that->n);
		T *c = new T[n1+1];
		for (int i = 0; i <= n1; i++)
			c[i] = 0;
		for (int i = 0; i <= min(this->n, that->n); i++)
			c[i] = this->a[i] + that->a[i];
		return poly(n1, c);
	}
	/*friend std::ostream & operator <<(std::ostream &out, poly other) {
		out << "Poly(" << other.n << ", ";
		for (int i = other.n; i >= 2; i--)
			out << other.a[i] << "*x^" << i << " + ";
		if (other.n > 0)
			out << other.a[1] << "*x + ";
		out << other.a[0] << " )";
		return out;
	}*/
	friend std::ostream & operator <<(std::ostream &out, poly other) {
		out << "Poly([" << other.a[0];
		for (int i = 1; i <= other.n; i++)
			out << ", " << other.a[i];
		out << "])";
		return out;
	}
};

int main()
{
	int n;
	std::cin >> n;
	double_pair points[n+1];  clock_t real_begin, real_end;
	for (int i = 0; i <= n; i++)
		std::cin >> points[i].fi >> points[i].se;
	for (int it = 0; it < 10; it++) {
		real_begin = clock();
		poly P = poly(n); poly L;
		for (int i = 0; i <= n; i++) {
			L = poly(0);
			L.a[0] = 1;
			for (int j = 0; j <= n; j++)
				if (i != j) 
					L = L * poly(1, 1.0, points[j].fi * (-1)) * (1.0 / (points[i].fi-points[j].fi));
			P = P + L * points[i].se;
		}
		real_end = clock();
		std::cout.precision(13);
		std::cout << std::fixed << n << ",lagr," << 1.0 * (real_end - real_begin) / CLOCKS_PER_SEC <<std::endl;
		std::cout << P <<std::endl;
	}
}
