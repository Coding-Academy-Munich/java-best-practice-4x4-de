package adventure.v1;

import java.util.Map;
import java.util.Objects;

public class Location {
    private final String name;
    private final String description;

    public Location(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public static Location fromDescription(Map<String, Object> description) {
        String name = (String) description.get("name");
        String desc = (String) description.getOrDefault("description", "");
        return new Location(name, desc);
    }

    @Override
    public String toString() {
        return "Location{" +
                "name='" + name + '\'' +
                ", description='" + description + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Location location = (Location) o;
        return Objects.equals(name, location.name) &&
                Objects.equals(description, location.description);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, description);
    }
}