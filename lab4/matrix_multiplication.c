#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gsl/gsl_ieee_utils.h>
#include <gsl/gsl_vector.h>
#include <gsl/gsl_blas.h>

const double min_val = 0.0, max_val = 1.0, scalar = 1.0;		//scalar = max_val - min_val;
clock_t realBegin, realEnd;

double get_double_rand() 
{
	return min_val + scalar * ((double)rand() / RAND_MAX);
}

gsl_matrix *rand_gsl_matrix(int rows, int cols)
{
	gsl_matrix *matrix = gsl_matrix_alloc(rows, cols);
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j< cols; j++) {
			  gsl_matrix_set(matrix, i, j, get_double_rand());
		}
	}
	return matrix;
}

double **rand_matrix(int rows, int cols)
{
    double **matrix = malloc(rows * sizeof(double*));
    for (int i = 0 ; i < rows; i++) {
        matrix[i] = malloc(cols * sizeof(double));
		for (int j = 0; j < cols; j++) 
			  matrix[i][j] = get_double_rand();
    }
    return matrix;
}

double **naive_matrix_multiplication(double **A, double **B, int rows, int cols, double *time)
{
	realBegin = clock();

	double **C = malloc(rows * sizeof(double*));
	for (int i = 0 ; i < rows ; i++)
		C[i] = calloc(cols, sizeof(double));

	for (int i = 0 ; i < cols; i++) {
		for (int j = 0 ; j < rows; j++) {
			for (int k = 0 ; k < cols; k++) {
				C[i][j] += A[i][k] * B[k][j];
			}
		}
	}

	realEnd = clock();
	*time = 1.0 * (realEnd - realBegin) / CLOCKS_PER_SEC;

  return C;
}

double **better_matrix_multiplication(double **A, double **B, int rows, int cols, double *time)
{
	realBegin = clock();
	
	double **C = malloc(rows * sizeof(double*));
	for (int i = 0; i < rows ; i++)
		C[i] = calloc(cols, sizeof(double));

	for (int i = 0; i < rows; i++) {
			for (int k = 0; k < cols; k++) {
				for (int j = 0; j < cols; j++) {
					C[i][j] += A[i][k] * B[k][j];
			}
		}
	}

	realEnd = clock();
	*time = 1.0 * (realEnd - realBegin) / CLOCKS_PER_SEC;

	return C;
}

gsl_matrix *blas_matrix_multiplication(gsl_matrix *A, gsl_matrix *B, int rows, int cols, double *time)
{
	realBegin = clock();

	gsl_matrix *C = gsl_matrix_alloc(rows,cols);

	if (gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, A, B, 0.0, C)) {
		fprintf(stderr, "Dot error");
	}

	realEnd = clock();
	*time = 1.0 * (realEnd - realBegin) / CLOCKS_PER_SEC;

	return C;
}


void free_2D_array(double **array, int rows, int cols) 
{
	for (int i = 0; i < rows; i++)
		free(array[i]);
	free(array);
}

int main()
{
	srand(time(NULL));

	char *csv_name = "matrix_multiplication_data.csv";
	FILE *csv_file = fopen(csv_name, "a");
	if(csv_file == NULL) {
		fprintf(stderr, "Could not open csv file");
		exit(1);
	}

	char *header = "real_time,function_type,matrix_size";
	char line[100];
	line[99]='\0';
	line[98]='a';

	fprintf(csv_file, "%s\r\n", header);

	int measurements = 10, n = 100, max_matrix_dim = 1200, step = 100, iteration = 1;
	double time;

	for (; n <= max_matrix_dim; n += step) {
		{
			gsl_matrix *A = rand_gsl_matrix(n, n);
			gsl_matrix *B = rand_gsl_matrix(n, n);
			gsl_matrix *C;
			printf("Testing n = %d:\n", iteration);
			iteration++;
			for (int j = 0; j < measurements; j++) {
				printf("Blas multiplication n: %d no.%d\n", n, j);
				C = blas_matrix_multiplication(A, B, n, n, &time);
				gsl_matrix_free(C);
				sprintf(line, "%.3lf,blas,%d", time, n);
				fprintf(csv_file, "%s\r\n", line);
			}
			gsl_matrix_free(A);
			gsl_matrix_free(B);
		}
		{
			double **A = rand_matrix(n, n);
			double **B = rand_matrix(n, n);
			double **C;

			for(int j = 0 ; j < measurements; j++) {
				printf("Naive multiplication n: %d no.%d\n", n, j);
				C = naive_matrix_multiplication(A, B, n, n, &time);
				free_2D_array(C, n, n);
				sprintf(line, "%.3lf,naive,%d", time, n);
				fprintf(csv_file, "%s\r\n", line);

				printf("Better multiplication n: %d no.%d\n", n, j);
				C = better_matrix_multiplication(A, B, n, n, &time);
				free_2D_array(C, n, n);
				sprintf(line, "%.3lf,better,%d", time, n);
				fprintf(csv_file, "%s\r\n", line);
			}
			free_2D_array(A, n, n);
			free_2D_array(B, n, n);
		}
	}

	fclose(csv_file);

	return 0;
}
