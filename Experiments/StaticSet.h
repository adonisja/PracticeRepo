template<typename T>
class StaticSet : public Collection<T>, public Object {
public:
    // Constructors
    StaticSet() : size(0), data(100) {}
    StaticSet(long s) : size(0), data(0) {
        if (s > 0) {
            data = Array<T>(s);
        } else {
            data = Array<T>(100);
        }
    }
    StaticSet(const StaticSet& other) : size(other.size), data(other.data) {}

    // Overloaded assignment operator
    StaticSet& operator=(const StaticSet& other) {
        if (this != &other) {
            size = other.size;
            data = other.data;
        }
        return *this;
    }

    // Destructor
    ~StaticSet() {}

    // Collection interface methods
    virtual void Insert(const T& element) override {
        if (!Contains(element) && !IsFull()) {
            data[size] = element;
            size++;
        }
    }

    virtual void Remove(const T& element) override {
        for (long i = 0; i < size; i++) {
            if (data[i] == element) {
                data[i] = data[size-1];
                size--;
                break;
            }
        }
    }

    virtual bool Contains(const T& element) const override {
        for (long i = 0; i < size; i++) {
            if (data[i] == element) {
                return true;
            }
        }
        return false;
    }

    virtual bool IsEmpty() const override {
        return size == 0;
    }

    virtual long Size() const override {
        return size;
    }

    // Other methods
    bool IsFull() const {
        return size == data.Length();
    }

    virtual std::string ToString() const override {
        std::string result = "{";
        for (long i = 0; i < size; i++) {
            result += std::to_string(data[i]);
            if (i < size - 1) {
                result += ", ";
            }
        }
        result += "}";
        return result;
    }

private:
    Array<T> data;
    long size;
};