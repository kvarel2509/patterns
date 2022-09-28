class Singleton {
	private static instance = null

	private constructor() {}

	public static newInstance() {
		if (this.instance === null) this.instance = new Singleton()
		return this.instance
	}
}


