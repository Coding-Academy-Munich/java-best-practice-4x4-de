// -*- coding: utf-8 -*-
// %% [markdown]
//
// <div style="text-align:center; font-size:200%;">
//  <b>Das JUnit Test-Framework</b>
// </div>
// <br/>
// <div style="text-align:center; font-size:120%;">Dr. Matthias Hölzl</div>
// <br/>
// <div style="text-align:center;">Coding-Akademie München</div>
// <br/>

// %% [markdown]
//
// ## Was ist JUnit?
//
// - JUnit ist ein modernes Test-Framework für Java
// - Open-Source
// - Einfach in Projekte zu integrieren
// - Viele Features
// - Struktur ähnlich zu xUnit-Test-Frameworks

// %% [markdown]
//
// ## Features von JUnit
//
// - Verwaltung von Tests und Test-Suites
// - Assertion-Bibliothek für Testfälle
// - Ausführung von Tests (Test Runner)
// - Unterstützung für Parameterized Tests

// %% [markdown]
//
// ## Assertions in JUnit
//
// - `assertTrue`, `assertFalse` um Bedingungen zu prüfen
// - `assertEquals`, `assertNotEquals` um Werte zu prüfen
// - `assertSame`, `assertNotSame` um auf Referenzen zu prüfen
// - `assertNull`, `assertNotNull` um auf `null` zu prüfen
// - `assertThrows` um Exceptions zu prüfen

// %%
// %maven org.junit.jupiter:junit-jupiter-api:5.8.2

// %%
import static org.junit.jupiter.api.Assertions.*;

// %%
assertTrue(5 > 3);

// %%
assertFalse(2 > 5);

// %%
// assertTrue(1 > 4);

// %%
assertEquals(4, 2 + 2);

// %%
assertNotEquals(5, 2 + 2);

// %%
String str1 = "Hello";
String str2 = "Hello";
String str3 = "World";

// %%
// assertSame(str1, str2);

// %%
assertSame(str1, str1);

// %%
// assertNotSame(str1, str1);

// %%
assertNull(null);

// %%
// assertNull(0);

// %%
assertNotNull(123);

// %%
assertThrows(ArithmeticException.class, () -> {
    int result = 1 / 0;
});

// %%
// assertThrows(ArithmeticException.class, () -> {
//     int result = 1 / 1;
// });


// %% [markdown]
//
// ## Die Testklasse
//
// - `@Test`-Annotation um Tests zu definieren
// - Assertions wie oben besprochen

// %%
// %maven org.junit.jupiter:junit-jupiter-api:5.8.2

// %%
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

// %%
public class JUnitBasicsTest {
    @Test
    public void testAddition() {
        assertEquals(4, 2 + 2);
    }

    @Test
    public void testTrueCondition() {
        assertTrue(5 > 3);
    }

    @Test
    public void testFalseCondition() {
        assertFalse(2 > 5);
    }

    @Test
    public void testException() {
        assertThrows(ArithmeticException.class, () -> {
            int result = 1 / 0;
        });
    }
}

// %%
JUnitBasicsTest tests = new JUnitBasicsTest();

// %%
tests.testAddition()

// %%
// %maven org.junit.jupiter:junit-jupiter-engine:5.8.2
// %maven org.junit.platform:junit-platform-launcher:1.9.0

// %%
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryRequest;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;
import static org.junit.platform.engine.discovery.DiscoverySelectors.selectClass;

// %%
LauncherDiscoveryRequest request = LauncherDiscoveryRequestBuilder.request()
    .selectors(selectClass(JUnitBasicsTest.class))
    .build();
Launcher launcher = LauncherFactory.create();
SummaryGeneratingListener listener = new SummaryGeneratingListener();

// %%
launcher.registerTestExecutionListeners(listener);
launcher.execute(request);

// %%
// Use StringWriter and PrintWriter to capture the summary output
StringWriter stringWriter = new StringWriter();
PrintWriter printWriter = new PrintWriter(stringWriter);
listener.getSummary().printTo(printWriter);

// %%
// Print the captured summary
System.out.println(stringWriter.toString());

// %%
// If you want more control over the output:
long testFoundCount = listener.getSummary().getTestsFoundCount();
long testFailedCount = listener.getSummary().getTestsFailedCount();


// %%
System.out.println("Total tests: " + testFoundCount);
System.out.println("Failed tests: " + testFailedCount);
System.out.println(testFailedCount == 0 ? "All tests passed!" : "Some tests failed.");

// %%
// Print details of failures
listener.getSummary().getFailures().forEach(failure -> {
    System.out.println("Failure in test: " + failure.getTestIdentifier().getDisplayName());
    System.out.println("Reason: " + failure.getException());
});

// %% [markdown]
//
// ## Ein einfacher Test mit JUnit im IDE
//
// - Starter-Kit: `code/starter_kits/junit_basics/`
// - Vollständige Implementierung: `code/complete/junit_basics/`

// %% [markdown]
//
// ### Maven-Projekt
//
// ```xml
// <dependency>
//   <groupId>org.junit.jupiter</groupId>
//   <artifactId>junit-jupiter</artifactId>
//   <version>RELEASE</version>
//   <scope>test</scope>
// </dependency>
// ```

// %% [markdown]
//
// ## Workshop: JUnit Basics
//
// Wir haben in den letzten Videos beispielhafte Tests für ein sehr einfaches
// Online-Shopping-System geschrieben ohne ein Test-Framework zu verwenden.
//
// Im Ordner `code/starter-kits/junit-order-sk/` finden Sie eine etwas
// erweiterte Version dieses Systems.
//
// Schreiben Sie dazu Tests mit JUnit.
//
// Bewerten Sie die Tests anhand der Kriterien, die wir in den letzten Videos
// besprochen haben.
